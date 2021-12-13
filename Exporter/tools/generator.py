# encoding=utf-8

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
    print('python version:', sys.version_info)
import os
import xlrd
import re
import collections
import json
import codecs
import importlib
import logging
import tools.utility as utility
import tools.script_exporter as script_exporter
import tools.string_script as string_script
import tools.custom_filed as custom_filed

# Define Const Files
Global_Sheet_Tile = ('name', 'type', 'value', 'sign', 'description')
Index_Name = 0
Index_Type = 1
Index_Value = 2
Index_Rule = 3
Index_Des = 4

Index_Item_Des = 0  # 列表的excel 第一行表示 注释
Index_Item_Type = 1  # 列表的excel 第二行表示 类型定义
Index_Item_Name = 2  # 列表的excel 第三行表示 字段名
Index_Item_Rule = 3  # 列表的excel 第四行表示 导出规则

BaseTypeInt = "int32"  # protoc基础类型 int
BaseTypeFloat = "float"  # protoc基础类型 float
BaseTypeDouble = "double"  # protoc基础类型 double
BaseTypeString = "string"  # protoc基础类型 string
BaseTypeBool = "bool"  # protoc基础类型 bool
BaseTypes = {'int': BaseTypeInt, 'float': BaseTypeFloat, 'double': BaseTypeDouble, 'string': BaseTypeString,
             'bool': BaseTypeBool}
BaseProtoTypes = {'int32': 'int'}
ETypeList = 'list'  # 标识枚举 数组类型
ETypeObj = 'obj'  # 标识枚举 对象类型
ETypeBase = 'base'  # 标识枚举 基础类型
SplitArray = ','  # 配置的
SplitObjArray = ';'  # 配置的
SplitTypeFiled = ';'  # 对象类型的字段数组分割  int a : int b
SplitValueFiled = ';'  # 对象类型的字段数组分割  10 : 100
SheetRowMaxSpaceCount = 3  # 连续空白几行  余下的不读取
IgnoreSign = '#'  # 注释行标识符
SplitArrayObjValue = r"{.*?}"  # 分割对象数组
OutDir_Protos = 'protos'  # 导出的proto文件所在的文件夹
OutDir_Jsons = 'json'  # 导出的json文件所在的文件夹
OutDir_Lua = 'lua'  # 导出的lua文件所在的文件夹
OutDir_Protobuf = 'protobuf'  # 导出的protobuf文件所在的文件夹
OutDir_Lua_Api = 'lua_api'  # 导出的LuaAPI文件所在的文件夹
ListSuffix = 'List'  # 列表类型尾缀
BooleanFalse = ('0', '0.0', 'false', 'False', 'off', 'Off', '', 'None')  # bool 类型 false 定义
BooleanTrue = ('1', '1.0', 'true', 'True', 'on', 'On')  # bool 类型 true 定义
LogEnable = True

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置


# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上

def log(*args):
    if LogEnable:
        utility.log(args)


def get_export_global_proto_folder():
    return OutDir_Protos


def get_export_protobuf_folder():
    return OutDir_Protobuf


def get_export_global_flat_folder():
    return "flat"


def is_match_rules(sheet_name, filed_name, rules):
    print(sheet_name, filed_name, rules)
    return True


class Exporter:
    def __init__(self, file_list, out_scripts, out_flatbuffer_scripts, out_data_formats, name_space, suffix):
        """

        :param file_list: 导出的excel 文件列表
        :param out_scripts: 导出的脚本
        :param out_data_formats: 导出的数据格式
        :param name_space: 导出脚本的命名空间
        :param suffix:   脚本尾缀
        """
        self.file_list = file_list
        self.out_data_formats = out_data_formats
        self.proto_infos = []
        self.global_msgs = []
        self.name_space = name_space
        self.suffix = suffix
        self.script_out_dic = out_scripts
        self.script_out_flatbuffer_dic = out_flatbuffer_scripts
        self.add_global_msg()

    def add_global_msg(self):
        file = 'custom.xlsx'
        self.add_global_file_msg(file)

    def add_global_file_msg(self, file):
        if not os.path.exists(file):
            log("if need a custom type,create a custom.xlsx file.")
            return
        try:
            excel_info = xlrd.open_workbook(file)
            sheet = excel_info.sheets()[0]
            msgs = Message("GlobalDefine", '', '', None, False)
            for index in range(1, sheet.nrows):
                row = sheet.row_values(index)
                if not script_exporter.is_ignore_row(row):
                    msgs.add_filed(row[0], row[1], row[2])
            for msg in msgs.child_msgs:
                msg.parent_msg = None
                msg.set_name(msg.get_name()[:-1])
                self.global_msgs.append(msg)
        except Exception as e:
            raise ValueError('export global fail!', e)

    # def register_global_msg(self):
    #     msgs = []
    #     msg = Message("Position2Int", '', '', None, False)
    #     msg.add_filed('X', 'int', 'x轴向')
    #     msg.add_filed('Y', 'int', 'y轴向')
    #     msgs.append(msg)
    #     return msgs

    def get_file_list_path(self):
        return self.file_list

    def get_script_tag(self):
        return self.export_script_tag

    def export(self):
        files = self.get_file_list_path()
        for excel_file in files:
            excel_data = xlrd.open_workbook(excel_file)
            for sheet in excel_data.sheets():
                export_mark_name = script_exporter.get_sheet_export_mark(sheet.name)
                if export_mark_name:
                    info = self.build_single_sheet_proto(export_mark_name, sheet)
                    self.proto_infos.append(info)
        self.export_proto()
        self.export_script()
        self.export_flat_scheme()
        self.export_flat_script()
        self.export_data()

    def export_proto(self):
        global_dir = get_export_global_proto_folder()
        proto_dir = script_exporter.get_export_proto_folder()
        utility.prepare_dir(global_dir)
        utility.prepare_dir(proto_dir)
        for msg in self.global_msgs:
            log("export global proto file:", msg.get_proto_file_name())
            msg.to_protobuf_proto(global_dir)
        for info in self.proto_infos:
            msg = info.get_message()
            log("export proto file:", msg.get_proto_file_name())
            msg.to_protobuf_proto(proto_dir)

    def export_flat_scheme(self):
        global_dir = get_export_global_flat_folder()
        proto_dir = get_export_global_flat_folder()
        utility.prepare_dir(global_dir)
        utility.prepare_dir(proto_dir)
        for msg in self.global_msgs:
            log("export global proto file:", msg.get_proto_file_name())
            msg.to_flat_scheme(global_dir)
        for info in self.proto_infos:
            msg = info.get_message()
            log("export flat file:", msg.get_proto_file_name())
            msg.to_flat_scheme(proto_dir)

    def export_script(self):
        if isinstance(self.script_out_dic, dict):
            for k, v in self.script_out_dic.items():
                utility.prepare_dir(v)
                self.execute_protoc_out_script(k, v)

    def export_flat_script(self):
        if isinstance(self.script_out_flatbuffer_dic, dict):
            for k, v in self.script_out_flatbuffer_dic.items():
                utility.prepare_dir(v)
                self.execute_flat_buffer_out_script(k, v)
                if k == "lua":
                    self.to_faltbuffer_lua_api(v)
                    pass

    def execute_protoc_out_script(self, script_out, folder):
        for msg in self.global_msgs:
            self.export_script_item(msg, script_out, folder)
        for info in self.proto_infos:
            msg = info.get_message()
            self.export_script_item(msg, script_out, folder)

    def execute_flat_buffer_out_script(self, script_out, folder):
        for msg in self.global_msgs:
            self.export_flat_script_item(msg, script_out, folder)
        for info in self.proto_infos:
            msg = info.get_message()
            self.export_flat_script_item(msg, script_out, folder)

    def export_script_item(self, msg, script_out, out_folder):
        log("generate protobuff script :", msg.get_proto_name())
        cmd = self.get_protoc_cmd(msg, script_out, out_folder)
        os.system(cmd)

    def export_flat_script_item(self, msg, script_out, out_folder):
        log("generate flatbuff script :", msg.get_proto_name())
        cmd = self.get_flat_cmd(msg, script_out, out_folder)
        os.system(cmd)

    def get_protoc_cmd(self, msg, script_out, out_folder):
        return 'protoc --%s=%s/ %s/%s' % (script_out, out_folder, script_exporter.get_export_proto_folder(), msg.get_proto_file_name())

    def get_flat_cmd(self, msg, script_out, out_folder):
        '''
        --gen-onefile in a file
        :param msg:
        :param script_out:
        :param out_folder:
        :return:
        '''
        cmd = 'flatc --%s --bfbs-comments -o %s %s/%s --gen-onefile' % (
            script_out, out_folder, get_export_global_flat_folder(), msg.get_flat_buffer_proto_file_name())
        print(cmd)
        # cmd = 'flatc --%s -n %s --gen-onefile' % ('csharp', msg.get_flat_buffer_proto_file_name())
        return cmd

    def export_data(self):
        for format, out_folder in self.out_data_formats.items():
            if format == 'lua':
                self.export_lua_api()
                self.export_lua_data(out_folder)
            elif format == 'json':
                self.export_json_data(out_folder)
            elif format == 'protobuf':
                self.export_protobuf_data(out_folder)
            elif format == 'flatbuffer':
                out_flat_json = out_folder + "_json"
                self.export_flat_json_data(out_flat_json)
                self.export_flat_bin_data(out_folder + "_bin", out_flat_json)
            else:
                raise ValueError("unknown export data format:", format, "lua or json or protobuf")

    def export_json_data(self, out_folder):
        json_dir = out_folder
        utility.prepare_dir(json_dir)
        for info in self.proto_infos:
            file_name = info.get_proto_name()
            json_file = json_dir + '/' + file_name
            self.save_to_json(json_file, info.get_value())

    def export_flat_json_data(self, out_folder):
        json_dir = out_folder
        utility.prepare_dir(json_dir)
        for info in self.proto_infos:
            file_name = info.get_proto_name()
            json_file = json_dir + '/' + file_name
            self.save_to_json(json_file, info.get_lower_value())

    def export_lua_data(self, out_folder):
        lua_dir = out_folder
        lua_dir_list = out_folder + '_list/'
        utility.prepare_dir(lua_dir)
        utility.prepare_dir(lua_dir + '_list/')
        for info in self.proto_infos:
            self.save_to_lua(lua_dir, info)
            self.save_to_lua_list(lua_dir_list, info)

    def export_protobuf_data(self, out_folder):
        self.execute_protoc_out_script('python_out', '.')
        protobuf_dir = out_folder
        utility.prepare_dir(protobuf_dir)
        for info in self.proto_infos:
            file_name = info.get_proto_name()
            proto_file = protobuf_dir + '/' + file_name
            self.save_to_protobuf_data(proto_file, file_name, info.get_value(), info.is_single())
        for root, dirs, files in os.walk(script_exporter.get_export_proto_folder()):
            for name in files:
                if (name.endswith(".py")):
                    os.remove(os.path.join(root, name))

    def export_flat_bin_data(self, out_folder, json_dir):
        for info in self.proto_infos:
            file_name = info.get_proto_name()
            json_file = json_dir + '/' + file_name + '.json'
            fbs = info.get_flat_buffer_proto_file_name()
            cmd = "flatc --binary -o %s %s/%s %s" % (out_folder, get_export_global_flat_folder(), fbs, json_file)
            print(cmd)
            os.system(cmd)
        pass

    def build_single_sheet_proto(self, export_mark_name, sheet):
        """
        :param export_mark_name: string
        :param sheet: sheet
        :return:
        """
        global_sheet_info = script_exporter.get_global_sheet_info(sheet)
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
            row_rules = sheet.row_values(Index_Item_Rule)

            filed_names = collections.OrderedDict()
            filed_types = collections.OrderedDict()

            ### record fileds
            for index, value in enumerate(row_names):
                filed_name = utility.strip_filed(value)
                if index < len(row_types):
                    filed_type = utility.strip_filed(row_types[index])
                    if filed_name.isalpha and len(utility.strip_filed(filed_name)) > 0:
                        if is_match_rules(sheet.name, filed_name, row_rules[index]):
                            filed_names[index] = filed_name
                            filed_types[index] = filed_type
                            filed_des = row_des[index] if index < len(row_des) else filed_name
                            msg.add_filed(filed_name, filed_type, filed_des)

            ### record datas
            export_obj_dic = collections.OrderedDict()
            export_obj = []
            space_row_count = 0
            for row_index in range(4, sheet.nrows):
                row_values = sheet.row_values(row_index)
                first_text = str(row_values[0]).strip()

                if utility.is_null_or_empty(first_text):
                    space_row_count += 1
                    if space_row_count >= 3:
                        break;
                else:
                    space_row_count = 0
                    if first_text[0] == '#':
                        continue
                    item_obj = collections.OrderedDict()
                    for key, value in filed_names.items():
                        filed_name = value
                        filed_type = filed_types[key]
                        filed_value = row_values[key] if len(row_values) > key else ''
                        msg.record_internal_filed(item_obj, filed_name, filed_type, filed_value)
                    export_obj.append(item_obj)
            export_obj_dic[msg.get_name()] = export_obj
            return msg, export_obj_dic
        except Exception as e:
            raise e

    def build_global_proto(self, proto_name, sheet, sheet_tile_info):
        try:
            msg = Message(proto_name, self.name_space, self.suffix, None, False)  # 创建一个Message Proto
            msg.add_global_msg(self.global_msgs)
            space_row_count = 0
            export_obj = collections.OrderedDict()
            for filed_index in range(1, sheet.nrows):
                row = sheet.row_values(filed_index)
                if not script_exporter.is_ignore_row(row):
                    filed_name = utility.strip_filed(row[sheet_tile_info[Index_Name]])
                    filed_type = utility.strip_filed(row[sheet_tile_info[Index_Type]])
                    filed_value = utility.strip_filed(row[sheet_tile_info[Index_Value]])
                    filed_des = utility.strip_filed(row[sheet_tile_info[Index_Des]])
                    filed_rule = utility.strip_filed(row[sheet_tile_info[Index_Rule]])
                    # if not filed_name and not filed_value and not filed_value:
                    if not filed_name and not filed_value:
                        space_row_count += 1
                        if space_row_count >= SheetRowMaxSpaceCount:
                            break
                        continue
                    if filed_name and filed_type:
                        space_row_count = 0
                        if is_match_rules(sheet.name, filed_name, filed_rule):
                            msg.add_filed(filed_name, filed_type, filed_des)
                            msg.record_internal_filed(export_obj, filed_name, filed_type, filed_value)

            return msg, export_obj
        except Exception as e:
            raise e

    def save_to_json(self, out_file_name, obj):
        file_name = out_file_name + '.json'
        log("save json data :", file_name)
        value = script_exporter.get_json_data(obj)
        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write(value)
        print("md5:" + utility.get_file_md5(file_name))

    def save_to_lua(self, out_dir, info):
        """
        :param out_dir: 导出的所在的文件夹
        :param  info:
        :return:
        """
        file_name = info.get_proto_name()
        lua_file = out_dir + '/' + file_name + '.lua'
        obj = info.get_value()
        log("save lua data :", lua_file)
        lua_data = script_exporter.get_lua_data(obj)
        lua_str = "".join(lua_data)
        with codecs.open(lua_file, 'w', 'utf-8') as f:
            f.write('---@type %s\n' % file_name)
            f.write('local %s = %s\n%s %s' % (file_name, lua_str, 'return', file_name))
        print("md5:" + utility.get_file_md5(lua_file))

    def save_to_lua_list(self, out_dir, info):
        file_name = info.get_proto_name()
        lua_file = out_dir + file_name + '.lua'
        obj = info.get_value()
        is_list = not info.is_single()
        lua_data = script_exporter.get_lua_data(obj)
        lua_str = None
        readonly_tip = "function (t, k, v) error('error write to a read-only table with key = ' .. tostring(k)..', " \
                       "value ='..tostring(v)) end "
        if is_list:
            lua_str = string_script.StringScript(script_exporter.get_proto_info_lua_list(info))
        else:
            lua_str = string_script.StringScript("local %s = {}" % file_name)
            fill = "".join(lua_data)
            lua_str.add_line('local %s__mt = %s' % (file_name, fill))
            lua_str.add_line(
                'local %s__mt__mt = {__index= %s__mt,__newindex = %s}' % (file_name, file_name, readonly_tip))
            lua_str.add_line('setmetatable(%s,%s__mt__mt)' % (file_name, file_name))
            lua_str.add_line("return %s" % file_name)
        with codecs.open(lua_file, 'w', 'utf-8') as f:
            f.write(lua_str.get_value())
            # f.write()
        print("md5:" + utility.get_file_md5(lua_file))

    def export_lua_api(self):
        api_dir = OutDir_Lua_Api
        utility.prepare_dir(api_dir)
        self.export_base_api(api_dir)
        for msg in self.global_msgs:
            log("export global lua api file:", msg.get_proto_file_name())
            msg.to_lua_api(api_dir)
        for info in self.proto_infos:
            msg = info.get_message()
            log("export lua api file:", msg.get_proto_file_name())
            msg.to_lua_api(api_dir)

    def to_faltbuffer_lua_api(self, lua_dir):
        class_row = 6
        class_meta_row = 7
        for root, dirs, files in os.walk(lua_dir):
            for name in files:
                if (name.endswith(".lua")):
                    filePath = os.path.join(root, name)
                    data = None
                    with open(filePath, "r") as f:
                        data = f.readlines()
                        class_name = name.replace(".lua", "")
                        class_meta_name = class_name + "__mt"
                        data[class_row] = '---@class %s : %s \n %s ' % (class_name, class_meta_name, data[class_row])
                        data[class_meta_row] = '---@class %s \n %s ' % (class_meta_name, data[class_meta_row])
                    if data:
                        with open(filePath, "w+") as f:
                            f.writelines(data)

    def export_base_api(self, out_dir):
        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + 'BaseType' + '.lua'
        base_int = '---@class int32 number'
        base_double = '---@class double number'
        base_float = '---@class float number'
        base_bool = '---@class bool boolean'
        value = '%s\n%s\n%s\n%s' % (base_int, base_double, base_float, base_bool)
        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write(value)

    def save_to_protobuf_data(self, out_file_name, py_file, obj, is_single):
        module_name = script_exporter.get_export_proto_folder()
        class_proto = importlib.import_module(module_name + '.' + py_file + '_pb2')
        class_type = None
        if is_single:
            class_type = getattr(class_proto, py_file)
        elif isinstance(obj, dict):
            class_type = getattr(class_proto, py_file + ListSuffix)
        if class_type:
            proto = script_exporter.dict2pb(class_type, obj)
            file_name = out_file_name + '.bytes'
            log("save protobuf data :", file_name)
            with codecs.open(file_name, 'wb') as f:
                f.write(proto.SerializeToString())
            print("md5:" + utility.get_file_md5(file_name))
        else:
            raise ValueError('export to protobuf error! proto:' + py_file)


class Message:
    def __init__(self, name, name_space, suffix, parent_msg, is_list_obj):
        """
        :param name: 生成的Message名字 如果非 root 即非 parent_msg，  生成的文件为 name.proto
        :param name_space: 生成的Message 的命名空间
        :param suffix: 生成的Message 尾缀 通常为模板等！
        :param parent_msg: 如果parent_msg 不为空 即为内部类
        :param is_list_obj: 如果是类是全局表 一张表即为数据， 否则是数组对象类
        """
        self.name = name
        self.name_space = name_space
        self.suffix = suffix
        self.fields_proto = collections.OrderedDict()  # 用于生成.proto 的 filed 列表
        self.parent_msg = parent_msg  # 从属哪个message
        self.child_msgs = []
        self.is_list_obj = is_list_obj
        self.import_msgs = []
        self.global_msgs = []

    def get_child_messages(self):
        return self.child_msgs

    def add_global_msg(self, msgs):
        self.global_msgs.extend(msgs)

    def try_get_global_msg(self, msg_name):
        for msg in self.global_msgs:
            if msg.get_proto_name() == msg_name:
                return msg
        return None

    def is_child_message(self):
        return self.parent_msg is not None

    def get_name(self):
        if self.is_list_obj:
            return self.name + 's'
        return self.name

    def set_name(self, name):
        self.name = name

    def get_proto_name(self):
        if self.is_list_obj:
            return self.name + 's' + self.suffix
        return self.name + self.suffix

    def get_proto_file_name(self):
        return self.get_proto_name() + '.proto'

    def get_flat_buffer_proto_file_name(self):
        return self.get_proto_name() + '.fbs'

    def get_msg_lua_api(self):
        api = '---@class %s ' % (self.name + self.suffix)
        for i, filed in enumerate(self.fields_proto.values()):
            api = script_exporter.add_line(api, filed.get_lua_api())
        # print(self.get_lua_script())
        return api

    def get_lua_script(self):
        script_define = string_script.StringScript("local %s = {}" % (self.get_proto_name()))
        script_define.add_line("local %s__mt = {}" % (self.get_proto_name()))
        return script_define.get_value()

    def get_msg_proto(self):
        """
        :return: .proto 文件描述
        """
        class_define = 'message %s {' % (self.get_proto_name())
        for i, filed in enumerate(self.fields_proto.values()):
            class_define = script_exporter.add_space_line(class_define, filed.get_define_proto(i + 1))
        for msg in self.child_msgs:
            class_define = script_exporter.add_space_line(class_define, msg.get_msg_proto())
        if self.is_child_message():
            class_define = script_exporter.add_line(class_define, '  }')
        else:
            class_define = script_exporter.add_line(class_define, '}')
        if self.is_list_obj and not self.is_child_message():
            list_define = 'message %s%s {' % (self.get_proto_name(), ListSuffix)
            filed = custom_filed.Filed(self.name, self.get_proto_name(), ListSuffix, True)
            list_define = script_exporter.add_space_line(list_define, filed.get_define_proto(1))
            list_define = script_exporter.add_line(list_define, '}')
            class_define = script_exporter.add_line(class_define, list_define)
        return class_define

    def is_root_message(self):
        return self.is_list_obj and not self.is_child_message()

    def get_msg_flat_scheme(self):
        """
               :return: .proto 文件描述
               """
        class_define = 'table %s {' % (self.get_proto_name())
        for i, filed in enumerate(self.fields_proto.values()):
            class_define = script_exporter.add_space_line(class_define, filed.get_define_flat_scheme())

        if self.is_child_message():
            class_define = script_exporter.add_line(class_define, '  }')
        else:
            class_define = script_exporter.add_line(class_define, '}')

        for msg in self.child_msgs:
            class_define = script_exporter.add_space_line(class_define, msg.get_msg_flat_scheme())

        if self.is_list_obj and not self.is_child_message():
            list_define = 'table %s%s {' % (self.get_proto_name(), ListSuffix)
            filed = custom_filed.Filed(self.name, self.get_proto_name(), ListSuffix, True)
            list_define = script_exporter.add_space_line(list_define, filed.get_define_flat_scheme())
            list_define = script_exporter.add_line(list_define, '}')
            class_define = script_exporter.add_line(class_define, list_define)
        return class_define

    def get_list_lua_api(self):
        if self.is_list_obj and not self.is_child_message():
            api = '---@class %s ' % (self.get_proto_name())
            filed = custom_filed.Filed(self.name, self.name + self.suffix, ListSuffix, True)
            api = script_exporter.add_line(api, filed.get_lua_api())
            return api
        return None

    def get_full_proto(self):
        info = 'syntax = "proto3";'
        if not utility.is_null_or_empty(self.name_space):
            info = script_exporter.add_line(info, "package %s;" % self.name_space)
        for msg_name in self.import_msgs:
            info = script_exporter.add_line(info, script_exporter.get_import_proto_define(msg_name))
        info = script_exporter.add_line(info, self.get_msg_proto())
        return info

    def get_full_flat_scheme(self):
        info = ''
        for msg_name in self.import_msgs:
            include_file = 'include "%s.fbs";' % msg_name
            if info == "":
                info = include_file
            else:
                info = script_exporter.add_line(info, include_file)

        if info == "":
            info = 'attribute "priority";'
        else:
            info = script_exporter.add_line(info, 'attribute "priority";')

        if not utility.is_null_or_empty(self.name_space):
            info = script_exporter.add_line(info, "namespace %s;" % self.name_space)

        info = script_exporter.add_line(info, self.get_msg_flat_scheme())
        if self.is_list_obj and not self.is_child_message():
            info = script_exporter.add_line(info, "root_type " + self.get_proto_name() + ListSuffix + ";")
        else:
            info = script_exporter.add_line(info, "root_type " + self.get_proto_name() + ";")
        return info

    def to_protobuf_proto(self, out_dir=''):
        """
        :param out_dir: 导出的文件夹
        :return:
        """
        file_name = ('%s/' % (out_dir) if len(
            out_dir) > 0 else '') + self.get_proto_file_name()  ## self.get_proto_name() + '.proto'
        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write(self.get_full_proto())

    def to_flat_scheme(self, out_dir=''):
        """
        :param out_dir: 导出的文件夹
        :return:
        """
        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + self.get_flat_buffer_proto_file_name()
        log(file_name)
        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write(self.get_full_flat_scheme())

    def to_lua_api(self, out_dir=''):
        list_sheet_api = self.get_list_lua_api()
        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + self.get_proto_name() + '.lua'
        if list_sheet_api:
            with codecs.open(file_name, 'w', 'utf-8') as f:
                f.write(list_sheet_api)

            template_api_name = self.name + self.suffix
            file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + template_api_name + '.lua'

        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write(self.get_msg_lua_api())

        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + self.get_proto_name() + '.'
        for msg in self.child_msgs:
            child_file_name = file_name + msg.get_proto_name() + '.lua'
            with codecs.open(child_file_name, 'w', 'utf-8') as f:
                f.write(msg.get_msg_lua_api())

    def get_class_info(self):
        info = []
        for filed in self.fields_proto.values():
            info.append(filed.scheme_info())
        return json.dumps(info, ensure_ascii=False, indent=2)

    def record_internal_filed(self, export_obj, filed_name, filed_type, filed_value):
        self.record_filed(export_obj, filed_name, filed_type, filed_value)

    def record_filed(self, export_data, filed_name, filed_type, filed_value):
        type_define = self.get_type_define(filed_type)
        if type_define == ETypeBase:
            self.record_base_value(export_data, filed_name, filed_type, filed_value)
        elif type_define == ETypeList:
            self.record_list_value(export_data, filed_name, filed_type, filed_value)
        elif type_define == ETypeObj:
            self.record_obj_value(export_data, filed_name, filed_type, filed_value)

    def record_base_value(self, parent, filed_name, filed_type, filed_value):
        base_type = self.get_type_name(filed_type, filed_name)
        value = script_exporter.convert(base_type, filed_value, filed_name)
        script_exporter.fill_value(parent, filed_name, value)

    def record_list_value(self, parent, filed_name, filed_type, filed_value):
        base_type, type_define = self.get_list_filed_info(filed_type)
        list_values = []
        values = []
        if type_define == ETypeList:
            raise ValueError('bug here!', filed_name, filed_type, filed_value)
        elif type_define == ETypeBase:
            if not utility.is_null_or_empty(filed_value):
                temps = str(filed_value).strip('[]').split(SplitArray)
                for v in temps:
                    values.append(script_exporter.convert(self.get_type_name(base_type, filed_name), v))
        elif type_define == ETypeObj:
            values = script_exporter.get_obj_value(filed_value)
        for v in values:
            self.record_filed(list_values, filed_name, base_type, v)
        script_exporter.fill_value(parent, filed_name + 's', list_values)

    def record_obj_value(self, parent, filed_name, filed_type, filed_value):
        obj = collections.OrderedDict()
        custom_message = self.try_get_global_msg(filed_type)
        filed_types = []
        if custom_message:
            custom_field_types = custom_message.get_msg_fields()
            for field in custom_field_types:
                filed_types.append(field.get_defined_type() + ' ' + field.get_name())
        else:
            filed_types.extend(script_exporter.get_obj_file_types(filed_type))
        values = str(filed_value).strip('{}').split(SplitValueFiled)
        if not utility.is_null_or_empty(values):
            for i in range(0, len(filed_types)):
                item_filed_type, item_filed_name = script_exporter.split_space(filed_types[i])
                v = values[i] if i < len(values) else ''
                self.record_filed(obj, item_filed_name, item_filed_type, v)
        else:
            log('record_obj_value is null:', filed_name)
        if utility.is_null_or_empty(filed_value):
            obj = None
        script_exporter.fill_value(parent, filed_name, obj)

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
        custom_msg = self.check_or_import_msg_type(filed_type)
        if custom_msg:
            self.build_filed_proto(filed_name, custom_msg.get_proto_name(), filed_des, is_array)
        else:
            class_name = utility.first_char_upper(filed_name) + '_'
            msg_item = Message(class_name, '', '', self, False)
            filed_types = script_exporter.get_obj_file_types(filed_type)
            for i in range(0, len(filed_types)):
                proto_filed_type, proto_filed_name = script_exporter.split_space(filed_types[i])
                msg_item.add_filed(proto_filed_name, proto_filed_type, proto_filed_name)
            msg = self.check_or_import_msg(msg_item)
            if msg:
                self.build_filed_proto(filed_name, msg.get_proto_name(), filed_des, is_array)
            else:
                self.build_filed_proto(filed_name, class_name, filed_des, is_array)
                self.child_msgs.append(msg_item)

    def check_or_import_msg_type(self, filed_type):
        custom_msg = self.try_get_global_msg(filed_type)
        if custom_msg:
            if not utility.is_in_list(self.import_msgs, custom_msg.get_proto_name()):
                self.import_msgs.append(custom_msg.get_proto_name())
        return custom_msg

    def check_or_import_msg(self, msg):
        info = msg.get_class_info()
        for child in self.child_msgs:
            if child.get_class_info() == info:
                return child
        for global_msg in self.global_msgs:
            if global_msg.get_class_info() == info:
                import_name = global_msg.get_proto_name()
                if not utility.is_in_list(self.import_msgs, import_name):
                    self.import_msgs.append(import_name)
                return global_msg
        return False

    def get_import_msgs(self):
        import_msgs = []
        for global_msg in self.global_msgs:
            import_name = global_msg.get_proto_name()
            if utility.is_in_list(self.import_msgs, import_name):
                import_msgs.append(global_msg)
        return import_msgs

    def get_all_msg(self):
        all_msgs = collections.OrderedDict()
        for msg in self.get_import_msgs():
            if all_msgs.__contains__(msg.get_proto_name()):
                raise ValueError("%s is already add in msg,may be define is same Name!!!" % msg.get_proto_name())
            all_msgs[msg.get_proto_name()] = msg
        for msg in self.child_msgs:
            if all_msgs.__contains__(msg.get_proto_name()):
                raise ValueError("%s is already add in msg,may be define is same Name!!!" % msg.get_proto_name())
            all_msgs[msg.get_proto_name()] = msg
        return all_msgs

    def get_msg_fields(self):
        fields = []
        for filed in self.fields_proto.values():
            fields.append(filed)
        return fields

    def build_filed_proto(self, filed_name, filed_type, filed_des, is_list):
        """
        构造message 文件内的字段
        :param filed_name: 字段名
        :param filed_type: 字段声明类型 （包含基础类型，数组，自定义对象等）
        :param filed_des:  字段描述 （即字段备注）
        :param is_list:    字段是否为数组
        :return:
        """
        filed = custom_filed.Filed(filed_name, filed_type, filed_des, is_list)
        self.fields_proto[filed.get_filed_name()] = filed
        return filed

    def get_type_define(self, filed_type):
        return script_exporter.get_type_define(filed_type, self)

    def get_type_name(self, filed_type, file_name):
        return script_exporter.get_type_name(filed_type, file_name, self)


class ProtoInfo:
    def __init__(self, msg, record_obj, is_single_sheet):
        self.message = msg
        self.record_obj = record_obj
        self.record_lower_obj = script_exporter.build_lower_obj(record_obj)
        self.is_single_sheet = is_single_sheet

    def get_proto_name(self):
        return self.message.get_proto_name()

    def get_flat_buffer_proto_file_name(self):
        return self.message.get_flat_buffer_proto_file_name()

    def get_message(self):
        return self.message

    def get_value(self):
        return self.record_obj

    def get_lower_value(self):
        return self.record_lower_obj

    def is_single(self):
        return self.is_single_sheet


def generator(file_list, out_protobuf_scripts, out_flatbuffer_scripts, out_data_formats, name_space, suffix):
    """

    :param file_list:  Excel Exports
    :param out_protobuf_scripts:  Scripts Formats: Dictionary  key is protoc cmd, value is out folder
    :param out_flatbuffer_scripts:  Scripts Formats: Dictionary  key is flatc cmd, value is out folder
    :param out_data_formats: Export datas; key is lua json or protobuf, value is out folder
    :param name_space: Scripts NameSpace
    :param suffix: ScriptClass Suffix
    :return:
    """
    export = Exporter(file_list, out_protobuf_scripts, out_flatbuffer_scripts, out_data_formats, name_space, suffix)
    export.export()
