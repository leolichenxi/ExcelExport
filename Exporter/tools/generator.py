﻿# encoding=utf-8

'''
Copyright 2020 li Chenxi(lichenxi3010@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import sys
print(sys.platform)
if sys.version_info < (3, 0):
    print('python version need more than 3.x')
    sys.exit(1)
else:
    print('python version:',sys.version_info)
import os
import xlrd
import re
import collections
import string
import json
import codecs
import importlib
from google.protobuf.descriptor import FieldDescriptor as FD

# Define Const Files
Global_Sheet_Tile = ('name', 'type', 'value', 'description')
Index_Name = 0
Index_Type = 1
Index_Value = 2
Index_Des = 3

Index_Item_Des = 0
Index_Item_Type = 1
Index_Item_Name = 2

BaseTypes = {
    'int': 'int32',
    'float': 'float',
    'double': 'double',
    'string': 'string',
    'bool': 'bool'
}

ETypeList = 'list'
ETypeObj = 'obj'
ETypeBase = 'base'

SplitArray = ','  # 配置的
SplitTypeFiled = ':'  # 对象类型的字段数组分割  10 : 100
SheetRowMaxSpaceCount = 3  # 连续空白几行  余下的不读取

OutDir_Protos = 'protos'
OutDir_Jsons = 'json'
OutDir_Lua = 'lua'
OutDir_Protobuf = 'protobuf'
ListSuffix = 'List'


def find_index(key, v_list):
    for index, item in enumerate(v_list):
        if item == key:
            return index
    return -1


def register_global_msg():
    msgs = []
    msg = Message("Position2Int", '', '', None, False)
    msg.add_filed('X', 'int', 'x轴向')
    msg.add_filed('Y', 'int', 'y轴向')
    msgs.append(msg)
    return msgs


def is_null_or_empty(v):
    return v == '' or v is None


def get_bool_value(is_true):
    if is_true:
        return 1
    return 0


def is_in_list(in_list, value):
    for i in in_list:
        if i == value:
            return True
    return False


def get_json_data(data):
    return json.dumps(data, ensure_ascii=False, indent=2)


def newline(count):
    return '\n' + '  ' * count


def prepare_dir(dir):
    if is_null_or_empty(dir):
        return
    if not os.path.isdir(dir):
        os.makedirs(dir)


def get_lua_data(obj, indent=1):
    if isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, str):
        yield json.dumps(obj, ensure_ascii=False)
    else:
        yield '{'
        is_list = isinstance(obj, list)
        is_first = True

        for i in obj:
            if is_first:
                is_first = False
            else:
                yield ','
            yield newline(indent)
            if not is_list:
                k = i
                i = obj[k]
                yield k
                yield ' = '
            for part in get_lua_data(i, indent + 1):
                yield part

        yield newline(indent - 1)
        yield '}'


def dict2pb(cls, adict, strict=False):
    """
    Takes a class representing the ProtoBuf Message and fills it with data from
    the dict.
    """
    obj = cls( )
    for field in obj.DESCRIPTOR.fields:
        if not field.label == field.LABEL_REQUIRED:
            continue
        if not field.has_default_value:
            continue
        if not field.name in adict:
            raise ValueError('Field "%s" missing from descriptor dictionary.' % field.name)
    field_names = set([field.name for field in obj.DESCRIPTOR.fields])
    if strict:
        for key in adict.keys( ):
            if key not in field_names:
                raise ValueError('Key "%s" can not be mapped to field in %s class.' % (key, type(obj)))
    for field in obj.DESCRIPTOR.fields:
        if not field.name in adict:
            continue
        msg_type = field.message_type
        if field.label == FD.LABEL_REPEATED:
            if field.type == FD.TYPE_MESSAGE:
                for sub_dict in adict[field.name]:
                    item = getattr(obj, field.name).add( )
                    item.CopyFrom(dict2pb(msg_type._concrete_class, sub_dict))
            else:
                map(getattr(obj, field.name).append, adict[field.name])
        else:
            if field.type == FD.TYPE_MESSAGE:
                value = dict2pb(msg_type._concrete_class, adict[field.name])
                getattr(obj, field.name).CopyFrom(value)
            else:
                try:
                    setattr(obj, field.name, adict[field.name])
                except Exception as e:
                    raise e
                    raise ValueError(field.type, field.name, adict[field.name])
    return obj


class Exporter:
    def __init__(self, file_list, out_scripts, name_space, suffix):
        """

        :param file_list: 导出的excel 文件列表
        :param out_scripts: 导出的脚本
        :param name_space: 导出脚本的命名空间
        :param suffix:   脚本尾缀
        """
        self.file_list = file_list
        self.proto_infos = []
        self.global_msgs = []
        self.name_space = name_space
        self.suffix = suffix
        self.script_out_dic = out_scripts

    def add_global_msg(self):
        for msg in register_global_msg( ):
            self.global_msgs.append(msg)

    def get_export_json_folder(self):
        return OutDir_Jsons

    def get_export_lua_folder(self):
        return OutDir_Lua

    def get_export_proto_folder(self):
        return OutDir_Protos

    def get_export_global_proto_folder(self):
        return OutDir_Protos

    def get_export_protobuf_folder(self):
        return OutDir_Protobuf

    def get_file_list_path(self):
        return self.file_list

    def get_script_tag(self):
        return self.export_script_tag

    def get_sheet_export_mark(self, sheet_name):
        """

        :param sheet_name:
        :return: sheet name
        """
        p = re.search('\|([a-zA-Z]\w+)', sheet_name)
        return p.group(1) if p else False

    def export(self):
        self.add_global_msg( )
        files = self.get_file_list_path( )
        for excel_file in files:
            excel_data = xlrd.open_workbook(excel_file)
            for sheet in excel_data.sheets( ):
                export_mark_name = self.get_sheet_export_mark(sheet.name)
                if export_mark_name:
                    info = self.build_single_sheet_proto(export_mark_name, sheet)
                    self.proto_infos.append(info)
        self.export_proto( )
        self.export_script( )
        self.export_data( )

    def export_proto(self):
        global_dir = self.get_export_global_proto_folder( )
        proto_dir = self.get_export_proto_folder( )
        prepare_dir(global_dir)
        prepare_dir(proto_dir)
        for msg in self.global_msgs:
            print("export global proto file:", msg.get_proto_file_name( ))
            msg.to_protobuf_proto(global_dir)
        for info in self.proto_infos:
            msg = info.get_message( )
            print("export proto file:", msg.get_proto_file_name( ))
            msg.to_protobuf_proto(proto_dir)

    def export_script(self):
        if isinstance(self.script_out_dic, dict):
            for k, v in self.script_out_dic.items( ):
                prepare_dir(v)
                self.execute_protoc_out_script(k, v)

    def execute_protoc_out_script(self, script_out, folder):
        for msg in self.global_msgs:
            self.export_script_item(msg, script_out, folder)
        for info in self.proto_infos:
            msg = info.get_message( )
            self.export_script_item(msg, script_out, folder)

    def export_script_item(self, msg, script_out, out_folder):
        print("generate script :", script_out, out_folder)
        cmd = self.get_protoc_cmd(msg, script_out, out_folder)
        os.system(cmd)

    def get_protoc_cmd(self, msg, script_out, out_folder):
        return 'protoc --%s=%s/ %s/%s' % (
            script_out, out_folder, self.get_export_proto_folder( ), msg.get_proto_file_name( ))

    def export_data(self):
        self.export_json_data( )
        self.export_lua_data( )
        self.export_protobuf_data( )

    def export_json_data(self):
        json_dir = self.get_export_json_folder( )
        prepare_dir(json_dir)
        for info in self.proto_infos:
            file_name = info.get_proto_name( )
            json_file = json_dir + '/' + file_name
            self.save_to_json(json_file, info.get_value( ))

    def export_lua_data(self):
        lua_dir = self.get_export_lua_folder( )
        prepare_dir(lua_dir)
        for info in self.proto_infos:
            file_name = info.get_proto_name( )
            lua_file = lua_dir + '/' + file_name
            self.save_to_lua(lua_file, info.get_value( ))

    def export_protobuf_data(self):
        self.execute_protoc_out_script('python_out', '.')
        protobuf_dir = self.get_export_protobuf_folder( )
        prepare_dir(protobuf_dir)
        for info in self.proto_infos:
            file_name = info.get_proto_name( )
            proto_file = protobuf_dir + '/' + file_name
            self.save_to_protobuf_data(proto_file, file_name, info.get_value( ), info.is_single( ))
        for root, dirs, files in os.walk(self.get_export_proto_folder( )):
            for name in files:
                if (name.endswith(".py")):
                    os.remove(os.path.join(root, name))

    def build_single_sheet_proto(self, export_mark_name, sheet):
        """
        :param export_mark_name: string
        :param sheet_info: sheet
        :return:
        """
        global_sheet_info = self.get_global_sheet_info(sheet)
        if global_sheet_info:
            msg, obj = self.build_global_proto(export_mark_name, sheet, global_sheet_info)
            return ProtoInfo(msg, obj, True)
        else:
            msg, obj = self.build_item_proto(export_mark_name, sheet)
            return ProtoInfo(msg, obj, False)

    def build_item_proto(self, proto_name, sheet):
        try:
            msg = Message(proto_name, self.name_space, self.suffix, None, True)
            msg.add_global_msg(self.global_msgs)
            row_des = sheet.row_values(Index_Item_Des)
            row_types = sheet.row_values(Index_Item_Type)
            row_names = sheet.row_values(Index_Item_Name)
            filed_names = collections.OrderedDict( )
            filed_types = collections.OrderedDict( )
            for index, value in enumerate(row_names):
                filed_name = self.strip_filed(value)
                if index < len(row_types):
                    filed_type = self.strip_filed(row_types[index])
                    if filed_name.isalpha and len(self.strip_filed(filed_name)) > 0:
                        filed_names[index] = filed_name
                        filed_types[index] = filed_type
                        filed_des = row_des[index] if index < len(row_des) else filed_name
                        msg.add_filed(filed_name, filed_type, filed_des)
            export_obj_dic = collections.OrderedDict( )
            export_obj = []
            space_row_count = 0
            for row_index in range(4, sheet.nrows):
                row_values = sheet.row_values(row_index)
                first_text = str(row_values[0]).strip( )
                if is_null_or_empty(first_text):
                    space_row_count += 1
                    if space_row_count >= 3:
                        break;
                else:
                    if first_text[0] == '#':
                        continue
                    item_obj = collections.OrderedDict( )
                    for key, value in filed_names.items( ):
                        filed_name = value
                        filed_type = filed_types[key]
                        filed_value = row_values[key] if len(row_values) > key else ''
                        msg.record_internal_filed(item_obj, filed_name, filed_type, filed_value)
                    export_obj.append(item_obj)
            export_obj_dic[msg.get_name( )] = export_obj
            return msg, export_obj_dic
        except Exception as e:
            raise e

    def build_global_proto(self, proto_name, sheet, sheet_tile_info):
        try:
            msg = Message(proto_name, self.name_space, self.suffix, None, False)  # 创建一个Message Proto
            msg.add_global_msg(self.global_msgs)
            space_row_count = 0
            export_obj = collections.OrderedDict( )
            for filed_index in range(1, sheet.nrows):
                row = sheet.row_values(filed_index)
                if not self.is_ignore_row(row):
                    filed_name = self.strip_filed(row[sheet_tile_info[Index_Name]])
                    filed_type = self.strip_filed(row[sheet_tile_info[Index_Type]])
                    filed_value = self.strip_filed(row[sheet_tile_info[Index_Value]])
                    filed_des = self.strip_filed(row[sheet_tile_info[Index_Des]])
                    if not filed_name and not filed_value and not filed_value:
                        space_row_count += 1
                        if space_row_count >= SheetRowMaxSpaceCount:
                            break
                        continue
                    if filed_name and filed_type:
                        msg.add_filed(filed_name, filed_type, filed_des)
                        msg.record_internal_filed(export_obj, filed_name, filed_type, filed_value)
            return msg, export_obj
        except Exception as e:
            raise e

    def save_to_json(self, out_file_name, obj):
        file_name = out_file_name + '.json'
        print("save json data :", file_name)
        value = get_json_data(obj)
        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write(value)

    def save_to_lua(self, out_file_name, obj):
        file_name = out_file_name + '.lua'
        print("save lua data :", file_name)
        lua_str = "".join(get_lua_data(obj))
        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write('return ')
            f.write(lua_str)
        pass

    def save_to_protobuf_data(self, out_file_name, py_file, obj, is_single):
        module_name = self.get_export_proto_folder( )
        class_proto = importlib.import_module(module_name + '.' + py_file + '_pb2')
        class_type = None
        if is_single:
            class_type = getattr(class_proto, py_file)
        elif isinstance(obj, dict):
            class_type = getattr(class_proto, py_file + ListSuffix)

        if class_type:
            proto = dict2pb(class_type, obj)
            file_name = out_file_name + '.byte'
            print("save protobuf data :", file_name)
            with codecs.open(file_name, 'wb') as f:
                f.write(proto.SerializeToString( ))
        else:
            raise ValueError('export to protobuf error! proto:' + py_file)

    @staticmethod
    def is_ignore_row(row):
        if row[0][0] == '#':
            return True
        return False

    @staticmethod
    def strip_filed(value):
        return str(value).strip( )

    @staticmethod
    def get_global_sheet_info(sheet):
        """

        :param sheet:
        :return:
        """
        rows = sheet.row_values(0)
        name_index = find_index(Global_Sheet_Tile[0], rows)
        type_index = find_index(Global_Sheet_Tile[1], rows)
        value_index = find_index(Global_Sheet_Tile[2], rows)
        des_index = find_index(Global_Sheet_Tile[3], rows)
        if name_index == -1 or type_index == -1 or value_index == -1:
            return None
        return (name_index, type_index, value_index, des_index)


class ProtoInfo:
    def __init__(self, msg, record_obj, is_single_sheet):
        self.message = msg
        self.record_obj = record_obj
        self.is_single_sheet = is_single_sheet

    def get_proto_name(self):
        return self.message.get_proto_name( )

    def get_message(self):
        return self.message

    def get_value(self):
        return self.record_obj

    def is_single(self):
        return self.is_single_sheet


class Message:
    def __init__(self, name, name_space, suffix, parent_msg, is_list_obj):
        """
        :param name: 生成的Message名字 如果非 root 即非 parent_msg，  生成的文件为 name.proto
        :param name_space: 生成的Message 的命名空间
        :param suffix: 生成的Message 尾缀 通常为模板等！
        :param parent_msg: 如果parent_msg 不为空 及为内部类
        :param is_list_obj: 如果是类是全局表 一张表即为数据， 否则是数组对象类
        """
        self.name = name
        self.name_space = name_space
        self.suffix = suffix
        self.fileds_proto = collections.OrderedDict( )  # 用于生成.proto 的 filed 列表
        self.parent_msg = parent_msg  # 从属哪个message
        self.child_msgs = []
        self.is_list_obj = is_list_obj
        self.import_msgs = []
        self.global_msgs = []

    def add_global_msg(self, msgs):
        self.global_msgs.extend(msgs)

    def is_child_message(self):
        return self.parent_msg is not None

    def get_name(self):
        if self.is_list_obj:
            return self.name + 's'
        return self.name

    def get_proto_name(self):
        if self.is_list_obj:
            return self.name + 's' + self.suffix
        return self.name + self.suffix

    def get_proto_file_name(self):
        return self.get_proto_name( ) + '.proto'

    def get_msg_proto(self):
        """
        :return: .proto 文件描述
        """
        class_define = 'message %s {' % (self.get_proto_name( ))
        for i, filed in enumerate(self.fileds_proto.values( )):
            class_define = self.add_space_line(class_define, filed.get_define_proto(i + 1))
        for msg in self.child_msgs:
            class_define = self.add_space_line(class_define, msg.get_msg_proto( ))
        if self.is_child_message( ):
            class_define = self.add_line(class_define, '  }')
        else:
            class_define = self.add_line(class_define, '}')
        if self.is_list_obj and not self.is_child_message( ):
            list_define = 'message %s%s {' % (self.get_proto_name( ), ListSuffix)
            filed = Filed(self.get_name( ), self.get_proto_name( ), ListSuffix, True)
            list_define = self.add_space_line(list_define, filed.get_define_proto(1))
            list_define = self.add_line(list_define, '}')
            class_define = self.add_line(class_define, list_define)
        return class_define

    def get_full_proto(self):
        info = 'syntax = "proto3";'
        if not is_null_or_empty(self.name_space):
            info = self.add_line(info, "package %s;" % (self.name_space))
        for msg in self.import_msgs:
            info = self.add_line(info, 'import "%s/%s.proto";' % (OutDir_Protos, msg))
        info = self.add_line(info, self.get_msg_proto( ))
        return info

    def to_protobuf_proto(self, out_dir=''):
        """
        :param out_dir: 导出的文件夹
        :return:
        """
        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + self.get_proto_name( ) + '.proto'
        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write(self.get_full_proto( ))

    @staticmethod
    def add_space_line(s, value):
        return '%s\n  %s' % (s, value)

    @staticmethod
    def add_line(s, value):
        return '%s\n%s' % (s, value)

    def get_class_info(self):
        info = []
        for filed in self.fileds_proto.values( ):
            info.append(filed.scheme_info( ))
        return json.dumps(info, ensure_ascii=False, indent=2)

    def record_internal_filed(self, export_obj, filed_name, filed_type, filed_value):

        self.record_filed(export_obj, filed_name, filed_type, filed_value)

    def record_filed(self, export_data, filed_name, filed_type, filed_value):
        if is_null_or_empty(filed_value):
            return
        type_define = self.get_type_define(filed_type)
        if type_define == ETypeBase:
            self.record_base_value(export_data, filed_name, filed_type, filed_value)
            pass
        elif type_define == ETypeList:
            self.record_list_value(export_data, filed_name, filed_type, filed_value)
        elif type_define == ETypeObj:
            self.record_obj_value(export_data, filed_name, filed_type, filed_value)
            pass

    def record_base_value(self, parent, filed_name, filed_type, filed_value):
        base_type = self.get_type_name(filed_type, filed_name)
        value = self.convert(base_type, filed_value)
        self.fill_value(parent, filed_name, value)

    def record_list_value(self, parent, filed_name, filed_type, filed_value):
        base_type, type_define = self.get_list_filed_info(filed_type)
        list_values = []
        values = str(filed_value).strip('[]').split(SplitArray)
        for v in values:
            self.record_filed(list_values, filed_name, base_type, v)
        self.fill_value(parent, filed_name + 's', list_values)

    def record_obj_value(self, parent, filed_name, filed_type, filed_value):
        obj = collections.OrderedDict( )
        filed_types = self.get_obj_file_types(filed_type)
        values = str(filed_value).strip('{}').split(':')
        if not is_null_or_empty(values):
            for i in range(0, len(filed_types)):
                item_filed_type, item_filed_name = self.split_space(filed_types[i])
                v = values[i] if i < len(values) else ''
                self.record_filed(obj, item_filed_name, item_filed_type, v)
        else:
            print(filed_name)
        self.fill_value(parent, filed_name, obj)

    @staticmethod
    def fill_value(parent, filed_name, filed_value):
        if isinstance(parent, list):
            parent.append(filed_value)
        else:
            parent[filed_name] = filed_value

    @staticmethod
    def convert(base_type, value):
        if base_type == 'bool':
            bool_value = str(value)
            if bool_value in ('0', 'false', 'False', 'off', 'Off', '', 'None'):
                return get_bool_value(False)
            elif bool_value in ('1', 'true', 'True', 'on', 'On'):
                return get_bool_value(True)
            else:
                print("error!!!", value)
        elif base_type == 'int32':
            if is_null_or_empty(value):
                return 0
            value = int(float(value))
        elif base_type == 'float':
            if is_null_or_empty(value):
                return 0
            value = float(value)
        elif base_type == 'double':
            if is_null_or_empty(value):
                return 0
            value = float(value)
        elif base_type == 'string':
            if is_null_or_empty(value):
                return ''
            value = str(value)
        return value

    def add_filed(self, filed_name, filed_type, filed_des):
        """
        如果字段类型为基本数据类型 int,float,double,string,bool  定义在 BaseTypes 中 则value直接相应数据
        如果字段类型为数组：
        1.首先为[] 如果为基础类型的数组 则每个元素转为相应数组 存为数组
        2.如果为对象素组 {}[]声明素组 素组内存放词典
        :param filed_name: 字段名
        :param filed_type: 字段类型
        :param filed_des: 字段描述
        :return:
        """
        self.build_filed(filed_name, filed_type, filed_des)

    def build_filed(self, filed_name, filed_type, filed_des, is_array=False):
        type_define = self.get_type_define(filed_type)
        if type_define == ETypeBase:
            proto_type = self.get_type_name(filed_type, filed_name)
            self.build_filed_proto(filed_name, proto_type, filed_des, is_array)
        elif type_define == ETypeList:
            self.build_list_filed(filed_name, filed_type, filed_des)
        elif type_define == ETypeObj:
            self.build_obj_filed(filed_name, filed_type, filed_des, is_array)

    def build_list_filed(self, filed_name, filed_type, filed_des):
        base_type, type_define = self.get_list_filed_info(filed_type)
        if type_define == ETypeBase:
            self.build_filed(filed_name, base_type, filed_des, True)
        elif type_define == ETypeObj:
            self.build_obj_filed(filed_name, base_type, filed_des, True)

    def get_list_filed_info(self, filed_type):
        base_type = filed_type[:-2]
        type_define = self.get_type_define(base_type)
        return base_type, type_define

    def build_obj_filed(self, filed_name, filed_type, filed_des, is_array=False):
        class_name = filed_name.capitalize( ) + '_'
        msgItem = Message(class_name, '', '', self, False)
        filed_types = self.get_obj_file_types(filed_type)
        for i in range(0, len(filed_types)):
            proto_filed_type, proto_filed_name = self.split_space(filed_types[i])
            msgItem.add_filed(proto_filed_name, proto_filed_type, proto_filed_name)
        pass
        msg = self.check_or_import_msg(msgItem)
        if msg:
            self.build_filed_proto(filed_name, msg.get_proto_name( ), filed_des, is_array)
        else:
            self.build_filed_proto(filed_name, class_name, filed_des, is_array)
            self.child_msgs.append(msgItem)

    def check_or_import_msg(self, msg):
        info = msg.get_class_info( )
        for child in self.child_msgs:
            if child.get_class_info( ) == info:
                return child
        for global_msg in self.global_msgs:
            if global_msg.get_class_info( ) == info:
                import_name = global_msg.get_proto_name( )
                if not is_in_list(self.import_msgs, import_name):
                    self.import_msgs.append(import_name)
                return global_msg
        return False

    @staticmethod
    def get_obj_file_types(filed_type):
        return filed_type.strip('{}').split(SplitTypeFiled)

    def build_filed_proto(self, filed_name, filed_type, filed_des, is_list):
        """
        构造message 文件内的字段
        :param filed_name: 字段名
        :param filed_type: 字段声明类型 （包含基础类型，数组，自定义对象等）
        :param filed_des:  字段描述 （即字段备注）
        :param is_list:    字段是否为数组
        :return:
        """
        filed = Filed(filed_name, filed_type, filed_des, is_list)
        self.fileds_proto[filed.get_filed_name( )] = filed
        return filed

    @staticmethod
    def get_type_define(filed_type):
        """
        获取字段定义类型
        :param filed_type:
        :return: ETypeList ETypeObj or ETypeBase

        """
        if filed_type[-2:] == '[]':
            return ETypeList
        elif filed_type[0] == '{' and filed_type[-1] == '}':
            return ETypeObj
        else:
            return ETypeBase

    def get_type_name(self, filed_type, file_name):
        """
        获取字段类型名
        如果是对象，则直接为 file_name + '_'
        如果是list 则递归调用得到名字
        如果是基础字段 则直接返回 BaseTypes
        :param filed_type:
        :param file_name:
        :return:
        """
        define_type = self.get_type_define(filed_type)
        if define_type == ETypeObj:
            return file_name + '_'
        elif define_type == ETypeList:
            return self.get_type_name(filed_type[:-2], file_name)
        elif define_type == ETypeBase:
            filed_type = filed_type.lower( )
            return BaseTypes[filed_type]

    @staticmethod
    def split_space(s):
        return re.split(r'[' + string.whitespace + ']+', s.strip( ))


class Filed:
    def __init__(self, filed_name, filed_type, filed_des, is_list=False):
        self.filed_name = filed_name
        self.filed_type = filed_type
        self.filed_des = filed_des.replace('\n', '')
        self.is_list = is_list
        pass

    def get_filed_name(self):
        if self.is_list:
            return self.filed_name + 's'
        return self.filed_name

    def get_filed_type(self):
        return self.filed_type

    def get_filed_des(self):
        return self.filed_des

    def get_define_proto(self, index):
        r = ''
        if self.is_list:
            r = ' repeated'
        return '%s %s %s = %s ; // % s' % (
            r, self.get_filed_type( ), self.get_filed_name( ), index, self.get_filed_des( ))

    def scheme_info(self):
        return json.dumps((self.get_filed_name( ), self.get_filed_type( )), ensure_ascii=False, indent=2)


def generator(file_list, out_scripts, name_space, suffix):
    export = Exporter(file_list, out_scripts, name_space, suffix)
    export.export( )
    os.system("pause")
