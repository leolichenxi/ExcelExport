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
if sys.version_info < (3,0):
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
Global_Sheet_Tile = ('name','type','value','description')
Index_Name = 0
Index_Type = 1
Index_Value = 2
Index_Des = 3
Index_Item_Des = 0   #列表的excel 第一行表示 注释
Index_Item_Type = 1  #列表的excel 第二行表示 类型定义
Index_Item_Name = 2  #列表的excel 第三行表示 字段名
BaseTypeInt = "int32"         #protoc基础类型 int
BaseTypeFloat = "float"       #protoc基础类型 float
BaseTypeDouble = "double"     #protoc基础类型 double
BaseTypeString = "string"     #protoc基础类型 string
BaseTypeBool = "bool"         #protoc基础类型 bool
BaseTypes = {'int':BaseTypeInt,'float':BaseTypeFloat,'double':BaseTypeDouble,'string':BaseTypeString,'bool':BaseTypeBool}
BaseProtoTypes = {'int32':'int'}
ETypeList = 'list'     #标识枚举 数组类型
ETypeObj = 'obj'       #标识枚举 对象类型
ETypeBase = 'base'     #标识枚举 基础类型
SplitArray = ','  # 配置的
SplitObjArray = ';'  # 配置的
SplitTypeFiled = ';'  # 对象类型的字段数组分割  int a : int b
SplitValueFiled = ';'  # 对象类型的字段数组分割  10 : 100
SheetRowMaxSpaceCount = 3  # 连续空白几行  余下的不读取
IgnoreSign = '#'        #注释行标识符
SplitArrayObjValue = r"{.*?}"  #分割对象数组
OutDir_Protos = 'protos'  # 导出的proto文件所在的文件夹
OutDir_Jsons = 'json'  # 导出的json文件所在的文件夹
OutDir_Lua = 'lua'  # 导出的lua文件所在的文件夹
OutDir_Protobuf = 'protobuf'  # 导出的protobuf文件所在的文件夹
OutDir_Lua_Api = 'lua_api'  # 导出的LuaAPI文件所在的文件夹
ListSuffix = 'List'    #列表类型尾缀
BooleanFalse = ('0','0.0','false','False','off','Off','','None')  #bool 类型 false 定义
BooleanTrue = ('1','1.0','true','True','on','On')                 #bool 类型 true 定义
LogEnable = True


def log(*args):
    if LogEnable:
        print(*args)

def find_index(key,v_list):
    for index,item in enumerate(v_list):
        if item == key:
            return index
    return -1

def is_null_or_empty(v):
    return v == '' or v is None

def get_bool_value(is_true):
    if is_true:
        return True
    return False

def handle_excel_str(value):
    v = str(value).replace('\\n','\n')
    return v

def is_in_list(in_list,value):
    for i in in_list:
        if i == value:
            return True
    return False

def first_char_upper(v):
    if is_null_or_empty(v):
        return v
    v = v[0].upper() + v[1:]
    return v

def newline(count):
    return '\n' + '  ' * count

def prepare_dir(dir):
    if is_null_or_empty(dir):
        return
    if not os.path.isdir(dir):
        os.makedirs(dir)

def get_json_data(data):
    return json.dumps(data,ensure_ascii = False,indent = 2)

def convert_to_lower_snake_cake(key):
    length = len(key)
    if length == 1:
        return key.lower()
    elif length >=2:
        new_key = key[0].lower()
        for i in range(1,length):
            if key[i].isupper():
                new_key = new_key + "_" + key[i].lower()
            else:
                new_key = new_key + key[i]
            pass
        return new_key
    return key

def get_lua_data(obj,indent = 1):
    if isinstance(obj,int) or isinstance(obj,float) or isinstance(obj,str):
        yield json.dumps(obj,ensure_ascii = False)
    else:
        yield '{'
        is_list = isinstance(obj,list)
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
            for part in get_lua_data(i,indent + 1):
                yield part

        yield newline(indent - 1)
        yield '}'

def dict2pb(cls,adict,strict = False):
    """
    Takes a class representing the ProtoBuf Message and fills it with data from
    the dict.
    """
    obj = cls()
    for field in obj.DESCRIPTOR.fields:
        if not field.label == field.LABEL_REQUIRED:
            continue
        if not field.has_default_value:
            continue
        if not field.name in adict:
            raise ValueError('Field "%s" missing from descriptor dictionary.' % field.name)
    field_names = set([field.name for field in obj.DESCRIPTOR.fields])
    if strict:
        for key in adict.keys():
            if key not in field_names:
                raise ValueError('Key "%s" can not be mapped to field in %s class.' % (key,type(obj)))
    for field in obj.DESCRIPTOR.fields:
        if not adict.__contains__(field.name):
            continue
        msg_type = field.message_type
        if field.label == FD.LABEL_REPEATED:
            if field.type == FD.TYPE_MESSAGE:
                for sub_dict in adict[field.name]:
                    item = getattr(obj,field.name).add()
                    item.CopyFrom(dict2pb(msg_type._concrete_class,sub_dict))
            else:
                for i in adict[field.name]:
                    getattr(obj,field.name).append(
                        i)  # map(getattr(obj, field.name).append, adict[field.name]) bug this function!

        else:
            if field.type == FD.TYPE_MESSAGE:
                value = dict2pb(msg_type._concrete_class,adict[field.name])
                getattr(obj,field.name).CopyFrom(value)
            else:
                try:
                    setattr(obj,field.name,adict[field.name])
                except Exception as e:
                    raise ValueError('setattr',field.type,field.name,adict[field.name],e)
    return obj

def get_sheet_export_mark(sheet_name):
    """
    :param sheet_name:
    :return: sheet name
    """
    p = re.search('\|([a-zA-Z]\w+)',sheet_name)
    return p.group(1) if p else False

def get_export_json_folder():
    return OutDir_Jsons

def get_export_lua_folder():
    return OutDir_Lua

def get_export_proto_folder():
    return OutDir_Protos

def get_export_global_proto_folder():
    return OutDir_Protos

def get_export_protobuf_folder():
    return OutDir_Protobuf

def get_export_global_flat_folder():
    return "flat"

def get_export_flat_data_folder():
    return "flat_data"

def is_ignore_row(row):
    if len(row[0]) == 0:
        log('empty row!',row)
        return True
    if len(row[0][0]) == 0:
        log('empty row!',row)
        return True
    if row[0][0] == IgnoreSign:
        return True
    return False

def strip_filed(value):
    return str(value).strip()

def get_global_sheet_info(sheet):
    """
    :param sheet:
    :return:
    """
    rows = sheet.row_values(0)
    name_index = find_index(Global_Sheet_Tile[0],rows)
    type_index = find_index(Global_Sheet_Tile[1],rows)
    value_index = find_index(Global_Sheet_Tile[2],rows)
    des_index = find_index(Global_Sheet_Tile[3],rows)
    if name_index == -1 or type_index == -1 or value_index == -1:
        return None
    return (name_index,type_index,value_index,des_index)


class Exporter:
    def __init__(self,file_list,out_scripts,out_flatbuffer_scripts,out_data_formats,name_space,suffix):
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

    def add_global_file_msg(self,file):
        if not os.path.exists(file):
            log("if need a custom type,create a custom.xlsx file.")
            return
        try:
            excel_info = xlrd.open_workbook(file)
            sheet = excel_info.sheets()[0]
            msgs = Message("GlobalDefine",'','',None,False)
            for index in range(1,sheet.nrows):
                row = sheet.row_values(index)
                if not is_ignore_row(row):
                    msgs.add_filed(row[0],row[1],row[2])
            for msg in msgs.child_msgs:
                msg.parent_msg = None
                msg.set_name(msg.get_name()[:-1])
                self.global_msgs.append(msg)
        except Exception as e:
            raise ValueError('export global fail!',e)

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
                export_mark_name = get_sheet_export_mark(sheet.name)
                if export_mark_name:
                    info = self.build_single_sheet_proto(export_mark_name,sheet)
                    self.proto_infos.append(info)
        self.export_proto()
        self.export_script()
        self.export_data()

        self.export_flat_scheme()
        self.export_flat_script()

    def export_proto(self):
        global_dir = get_export_global_proto_folder()
        proto_dir = get_export_proto_folder()
        prepare_dir(global_dir)
        prepare_dir(proto_dir)
        for msg in self.global_msgs:
            log("export global proto file:",msg.get_proto_file_name())
            msg.to_protobuf_proto(global_dir)
        for info in self.proto_infos:
            msg = info.get_message()
            log("export proto file:",msg.get_proto_file_name())
            msg.to_protobuf_proto(proto_dir)

    def export_flat_scheme(self):
        global_dir = get_export_global_flat_folder()
        proto_dir = get_export_global_flat_folder()
        prepare_dir(global_dir)
        prepare_dir(proto_dir)
        for msg in self.global_msgs:
            log("export global proto file:",msg.get_proto_file_name())
            msg.to_flat_scheme(global_dir)
        for info in self.proto_infos:
            msg = info.get_message()
            log("export flat file:",msg.get_proto_file_name())
            msg.to_flat_scheme(proto_dir)

    def export_script(self):
        if isinstance(self.script_out_dic,dict):
            for k,v in self.script_out_dic.items():
                prepare_dir(v)
                self.execute_protoc_out_script(k,v)

    def export_flat_script(self):
        if isinstance(self.script_out_flatbuffer_dic,dict):
            for k,v in self.script_out_flatbuffer_dic.items():
                prepare_dir(v)
                self.execute_flat_buffer_out_script(k,v)

    def execute_protoc_out_script(self,script_out,folder):
        for msg in self.global_msgs:
            self.export_script_item(msg,script_out,folder)
        for info in self.proto_infos:
            msg = info.get_message()
            self.export_script_item(msg,script_out,folder)

    def execute_flat_buffer_out_script(self,script_out,folder):
        for msg in self.global_msgs:
            self.export_flat_script_item(msg,script_out,folder)
        for info in self.proto_infos:
            msg = info.get_message()
            self.export_flat_script_item(msg,script_out,folder)

    def export_script_item(self,msg,script_out,out_folder):
        log("generate protobuff script :",msg.get_proto_name())
        cmd = self.get_protoc_cmd(msg,script_out,out_folder)
        os.system(cmd)

    def export_flat_script_item(self,msg,script_out,out_folder):
        log("generate flatbuff script :",msg.get_proto_name())
        cmd = self.get_flat_cmd(msg,script_out,out_folder)
        os.system(cmd)

    def get_protoc_cmd(self,msg,script_out,out_folder):
        return 'protoc --%s=%s/ %s/%s' % (script_out,out_folder,get_export_proto_folder(),msg.get_proto_file_name())

    def get_flat_cmd(self, msg, script_out, out_folder):
        '''
        --gen-onefile in a file
        :param msg:
        :param script_out:
        :param out_folder:
        :return:
        '''
        cmd = 'flatc --%s -o %s %s/%s --gen-onefile' % (script_out,out_folder,get_export_global_flat_folder(), msg.get_flat_buffer_proto_file_name())
        print(cmd)
        # cmd = 'flatc --%s -n %s --gen-onefile' % ('csharp', msg.get_flat_buffer_proto_file_name())
        return cmd

    def export_data(self):
        for format,out_folder in self.out_data_formats.items():
            if format == 'lua':
                self.export_lua_api()
                self.export_lua_data(out_folder)
            elif format == 'json':
                self.export_json_data(out_folder)
            elif format == 'protobuf':
                self.export_protobuf_data(out_folder)
            elif format == 'flatbuffer':
                self.export_flat_json_data(out_folder+"_json")
                self.export_flat_bin_data(out_folder+"_bin",out_folder+"_json")
            else:
                raise ValueError("unknown export data format:",format,"lua or json or protobuf")

    def export_json_data(self,out_folder):
        json_dir = out_folder
        prepare_dir(json_dir)
        for info in self.proto_infos:
            file_name = info.get_proto_name()
            json_file = json_dir + '/' + file_name
            self.save_to_json(json_file,info.get_value())

    def export_flat_json_data(self, out_folder):
        json_dir = out_folder
        prepare_dir(json_dir)
        for info in self.proto_infos:
            file_name = info.get_proto_name()
            json_file = json_dir + '/' + file_name
            self.save_to_json(json_file,info.get_lower_value())

    def export_lua_data(self,out_folder):
        lua_dir = out_folder
        prepare_dir(lua_dir)
        for info in self.proto_infos:
            self.save_to_lua(lua_dir,info)

    def export_protobuf_data(self,out_folder):
        self.execute_protoc_out_script('python_out','.')
        protobuf_dir = out_folder
        prepare_dir(protobuf_dir)
        for info in self.proto_infos:
            file_name = info.get_proto_name()
            proto_file = protobuf_dir + '/' + file_name
            self.save_to_protobuf_data(proto_file,file_name,info.get_value(),info.is_single())
        for root,dirs,files in os.walk(get_export_proto_folder()):
            for name in files:
                if (name.endswith(".py")):
                    os.remove(os.path.join(root,name))

    def export_flat_bin_data(self, out_folder,json_dir):
        for info in self.proto_infos:
            file_name = info.get_proto_name()
            json_file = json_dir + '/' + file_name +'.json'
            fbs = info.get_flat_buffer_proto_file_name()
            cmd = "flatc --binary -o %s %s/%s %s" %(out_folder,get_export_global_flat_folder(),fbs,json_file)
            print(cmd)
            os.system(cmd)
        pass

    def build_single_sheet_proto(self,export_mark_name,sheet):
        """
        :param export_mark_name: string
        :param sheet_info: sheet
        :return:
        """
        global_sheet_info = get_global_sheet_info(sheet)
        if global_sheet_info:
            msg,obj = self.build_global_proto(export_mark_name,sheet,global_sheet_info)
            return ProtoInfo(msg,obj,True)
        else:
            msg,obj = self.build_item_proto(export_mark_name,sheet)
            return ProtoInfo(msg,obj,False)

    def build_item_proto(self,proto_name,sheet):
        try:
            msg = Message(proto_name,self.name_space,self.suffix,None,True)
            msg.add_global_msg(self.global_msgs)
            row_des = sheet.row_values(Index_Item_Des)
            row_types = sheet.row_values(Index_Item_Type)
            row_names = sheet.row_values(Index_Item_Name)
            filed_names = collections.OrderedDict()
            filed_types = collections.OrderedDict()
            for index,value in enumerate(row_names):
                filed_name = strip_filed(value)
                if index < len(row_types):
                    filed_type = strip_filed(row_types[index])
                    if filed_name.isalpha and len(strip_filed(filed_name)) > 0:
                        filed_names[index] = filed_name
                        filed_types[index] = filed_type
                        filed_des = row_des[index] if index < len(row_des) else filed_name
                        msg.add_filed(filed_name,filed_type,filed_des)
            export_obj_dic = collections.OrderedDict()
            export_obj = []
            space_row_count = 0
            for row_index in range(4,sheet.nrows):
                row_values = sheet.row_values(row_index)
                first_text = str(row_values[0]).strip()
                if is_null_or_empty(first_text):
                    space_row_count += 1
                    if space_row_count >= 3:
                        break;
                else:
                    if first_text[0] == '#':
                        continue
                    item_obj = collections.OrderedDict()
                    for key,value in filed_names.items():
                        filed_name = value
                        filed_type = filed_types[key]
                        filed_value = row_values[key] if len(row_values) > key else ''
                        msg.record_internal_filed(item_obj,filed_name,filed_type,filed_value)
                    export_obj.append(item_obj)
            export_obj_dic[msg.get_name()] = export_obj
            return msg,export_obj_dic
        except Exception as e:
            raise e

    def build_global_proto(self,proto_name,sheet,sheet_tile_info):
        try:
            msg = Message(proto_name,self.name_space,self.suffix,None,False)  # 创建一个Message Proto
            msg.add_global_msg(self.global_msgs)
            space_row_count = 0
            export_obj = collections.OrderedDict()
            for filed_index in range(1,sheet.nrows):
                row = sheet.row_values(filed_index)
                if not is_ignore_row(row):
                    filed_name = strip_filed(row[sheet_tile_info[Index_Name]])
                    filed_type = strip_filed(row[sheet_tile_info[Index_Type]])
                    filed_value = strip_filed(row[sheet_tile_info[Index_Value]])
                    filed_des = strip_filed(row[sheet_tile_info[Index_Des]])
                    if not filed_name and not filed_value and not filed_value:
                        space_row_count += 1
                        if space_row_count >= SheetRowMaxSpaceCount:
                            break
                        continue
                    if filed_name and filed_type:
                        msg.add_filed(filed_name,filed_type,filed_des)
                        msg.record_internal_filed(export_obj,filed_name,filed_type,filed_value)

            return msg,export_obj
        except Exception as e:
            raise e

    def save_to_json(self,out_file_name,obj):
        file_name = out_file_name + '.json'
        log("save json data :",file_name)
        value = get_json_data(obj)
        with codecs.open(file_name,'w','utf-8') as f:
            f.write(value)

    def save_to_lua(self,out_dir,info):
        """
        :param out_dir: 导出的所在的文件夹
        :param info: ProtoInfo
        :return:
        """
        file_name = info.get_proto_name()
        lua_file = out_dir + '/' + file_name + '.lua'
        obj = info.get_value()
        log("save lua data :",lua_file)
        lua_str = "".join(get_lua_data(obj))
        with codecs.open(lua_file,'w','utf-8') as f:
            f.write('---@type %s\n' % file_name)
            f.write('local %s = %s\n%s %s' % (file_name,lua_str,'return',file_name))

    def export_lua_api(self):
        api_dir = OutDir_Lua_Api
        prepare_dir(api_dir)
        self.export_base_api(api_dir)
        for msg in self.global_msgs:
            log("export global lua api file:",msg.get_proto_file_name())
            msg.to_lua_api(api_dir)
        for info in self.proto_infos:
            msg = info.get_message()
            log("export lua api file:",msg.get_proto_file_name())
            msg.to_lua_api(api_dir)

    def export_base_api(self,out_dir):
        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + 'BaseType' + '.lua'
        base_int = '---@class int32 number'
        base_double = '---@class double number'
        base_float = '---@class float number'
        base_bool = '---@class bool boolean'
        value = '%s\n%s\n%s\n%s' % (base_int,base_double,base_float,base_bool)
        with codecs.open(file_name,'w','utf-8') as f:
            f.write(value)

    def save_to_protobuf_data(self,out_file_name,py_file,obj,is_single):
        module_name = get_export_proto_folder()
        class_proto = importlib.import_module(module_name + '.' + py_file + '_pb2')
        class_type = None
        if is_single:
            class_type = getattr(class_proto,py_file)
        elif isinstance(obj,dict):
            class_type = getattr(class_proto,py_file + ListSuffix)
        if class_type:
            proto = dict2pb(class_type,obj)
            file_name = out_file_name + '.bytes'
            log("save protobuf data :",file_name)
            with codecs.open(file_name,'wb') as f:
                f.write(proto.SerializeToString())
        else:
            raise ValueError('export to protobuf error! proto:' + py_file)


def add_space_line(s,value):
    return '%s\n  %s' % (s,value)


def add_line(s,value):
    return '%s\n%s' % (s,value)


def fill_value(parent,filed_name,filed_value):
    if isinstance(parent,list):
        parent.append(filed_value)
    else:
        parent[filed_name] = filed_value


def convert(base_type,value,filed_name = None):
    if base_type == BaseTypeBool:
        bool_value = str(value)
        if bool_value in BooleanFalse:
            return get_bool_value(False)
        elif bool_value in BooleanTrue:
            return get_bool_value(True)
        else:
            raise ValueError("error!!!",base_type,filed_name,value)
    elif base_type == BaseTypeInt:
        if is_null_or_empty(value):
            return 0
        value = int(float(value))
    elif base_type == BaseTypeFloat:
        if is_null_or_empty(value):
            return 0
        value = float(value)
    elif base_type == BaseTypeDouble:
        if is_null_or_empty(value):
            return 0
        value = float(value)
    elif base_type == BaseTypeString:
        if is_null_or_empty(value):
            return ''
        value = handle_excel_str(value)
        value = str(value)
    else:
        raise ValueError("convert error! unknown type:",base_type,value,filed_name)
    return value


def get_obj_file_types(filed_type):
    return filed_type.strip('{}').split(SplitObjArray)


def split_space(s):
    return re.split(r'[' + string.whitespace + ']+',s.strip())


class Message:
    def __init__(self,name,name_space,suffix,parent_msg,is_list_obj):
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
        self.fileds_proto = collections.OrderedDict()  # 用于生成.proto 的 filed 列表
        self.parent_msg = parent_msg  # 从属哪个message
        self.child_msgs = []
        self.is_list_obj = is_list_obj
        self.import_msgs = []
        self.global_msgs = []

    def get_child_messages(self):
        return self.child_msgs

    def add_global_msg(self,msgs):
        self.global_msgs.extend(msgs)

    def try_get_global_msg(self,msg_name):
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

    def set_name(self,name):
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
        for i,filed in enumerate(self.fileds_proto.values()):
            api = add_line(api,filed.get_lua_api())
        return api

    def get_msg_proto(self):
        """
        :return: .proto 文件描述
        """
        class_define = 'message %s {' % (self.get_proto_name())
        for i,filed in enumerate(self.fileds_proto.values()):
            class_define = add_space_line(class_define,filed.get_define_proto(i + 1))
        for msg in self.child_msgs:
            class_define = add_space_line(class_define,msg.get_msg_proto())
        if self.is_child_message():
            class_define = add_line(class_define,'  }')
        else:
            class_define = add_line(class_define,'}')
        if self.is_list_obj and not self.is_child_message():
            list_define = 'message %s%s {' % (self.get_proto_name(),ListSuffix)
            filed = Filed(self.name,self.get_proto_name(),ListSuffix,True)
            list_define = add_space_line(list_define,filed.get_define_proto(1))
            list_define = add_line(list_define,'}')
            class_define = add_line(class_define,list_define)
        return class_define

    def get_msg_flat_scheme(self):
        """
               :return: .proto 文件描述
               """
        class_define = 'table %s {' % (self.get_proto_name())
        for i,filed in enumerate(self.fileds_proto.values()):
            class_define = add_space_line(class_define,filed.get_define_flat_scheme())

        if self.is_child_message():
            class_define = add_line(class_define,'  }')
        else:
            class_define = add_line(class_define,'}')

        for msg in self.child_msgs:
            class_define = add_space_line(class_define, msg.get_msg_flat_scheme())

        if self.is_list_obj and not self.is_child_message():
            list_define = 'table %s%s {' % (self.get_proto_name(),ListSuffix)
            filed = Filed(self.name,self.get_proto_name(),ListSuffix,True)
            list_define = add_space_line(list_define,filed.get_define_flat_scheme())
            list_define = add_line(list_define,'}')
            class_define = add_line(class_define,list_define)
        return class_define


    def get_list_lua_api(self):
        if self.is_list_obj and not self.is_child_message():
            api = '---@class %s ' % (self.get_proto_name())
            filed = Filed(self.name,self.name + self.suffix,ListSuffix,True)
            api = add_line(api,filed.get_lua_api())
            return api
        return None

    def get_full_proto(self):
        info = 'syntax = "proto3";'
        if not is_null_or_empty(self.name_space):
            info = add_line(info,"package %s;" % (self.name_space))
        for msg in self.import_msgs:
            info = add_line(info,'import "%s/%s.proto";' % (get_export_proto_folder(),msg))
        info = add_line(info,self.get_msg_proto())
        return info

    def get_full_flat_scheme(self):
        info = ''
        for msg in self.import_msgs:
            include_file = 'include "%s.fbs";' % (msg)
            if info == "":
                info = include_file
            else:
                info = add_line(info,include_file)

        if info == "":
            info = 'attribute "priority";'
        else:
            info = add_line(info, 'attribute "priority";')

        if not is_null_or_empty(self.name_space):
            info = add_line(info,"namespace %s;" % (self.name_space))

        info = add_line(info,self.get_msg_flat_scheme())
        if self.is_list_obj and not self.is_child_message():
            info = add_line(info,"root_type " +self.get_proto_name()+ListSuffix +";")
        else:
            info = add_line(info,"root_type " + self.get_proto_name() +";")
        return info


    def to_protobuf_proto(self,out_dir = ''):
        """
        :param out_dir: 导出的文件夹
        :return:
        """
        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + self.get_proto_file_name()  ## self.get_proto_name() + '.proto'
        with codecs.open(file_name,'w','utf-8') as f:
            f.write(self.get_full_proto())

    def to_flat_scheme(self,out_dir = ''):
        """
        :param out_dir: 导出的文件夹
        :return:
        """
        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + self.get_flat_buffer_proto_file_name()
        log(file_name)
        with codecs.open(file_name,'w','utf-8') as f:
            f.write(self.get_full_flat_scheme())

    def to_lua_api(self,out_dir = ''):
        list_sheet_api = self.get_list_lua_api()
        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + self.get_proto_name() + '.lua'
        if list_sheet_api:
            with codecs.open(file_name,'w','utf-8') as f:
                f.write(list_sheet_api)

            template_api_name = self.name + self.suffix
            file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + template_api_name + '.lua'

        with codecs.open(file_name,'w','utf-8') as f:
            f.write(self.get_msg_lua_api())

        file_name = ('%s/' % (out_dir) if len(out_dir) > 0 else '') + self.get_proto_name() + '.'
        for msg in self.child_msgs:
            child_file_name = file_name + msg.get_proto_name() + '.lua'
            with codecs.open(child_file_name,'w','utf-8') as f:
                f.write(msg.get_msg_lua_api())

    def get_class_info(self):
        info = []
        for filed in self.fileds_proto.values():
            info.append(filed.scheme_info())
        return json.dumps(info,ensure_ascii = False,indent = 2)

    def record_internal_filed(self,export_obj,filed_name,filed_type,filed_value):
        self.record_filed(export_obj,filed_name,filed_type,filed_value)

    def record_filed(self,export_data,filed_name,filed_type,filed_value):
        if is_null_or_empty(filed_value):
            return
        type_define = self.get_type_define(filed_type)
        if type_define == ETypeBase:
            self.record_base_value(export_data,filed_name,filed_type,filed_value)
        elif type_define == ETypeList:
            self.record_list_value(export_data,filed_name,filed_type,filed_value)
        elif type_define == ETypeObj:
            self.record_obj_value(export_data,filed_name,filed_type,filed_value)

    def record_base_value(self,parent,filed_name,filed_type,filed_value):
        base_type = self.get_type_name(filed_type,filed_name)
        value = convert(base_type,filed_value,filed_name)
        fill_value(parent,filed_name,value)

    def record_list_value(self,parent,filed_name,filed_type,filed_value):
        base_type,type_define = self.get_list_filed_info(filed_type)
        list_values = []
        values = []
        if type_define == ETypeList:
            raise ValueError('bug here!',filed_name,filed_type,filed_value)
        elif type_define == ETypeBase:
            values = str(filed_value).strip('[]').split(SplitArray)
        elif type_define == ETypeObj:
            values = re.findall(SplitArrayObjValue,str(filed_value))  ##--str(filed_value).strip('[]').split(SplitObjArray)
        for v in values:
            self.record_filed(list_values,filed_name,base_type,v)
        fill_value(parent,filed_name + 's',list_values)

    def record_obj_value(self,parent,filed_name,filed_type,filed_value):
        obj = collections.OrderedDict()
        custom_message = self.try_get_global_msg(filed_type)
        filed_types = []
        if custom_message:
            custom_field_types = custom_message.get_msg_file_types()
            for field in custom_field_types:
                filed_types.append(field.get_defined_type() + ' ' + field.get_name())
        else:
            filed_types.extend(get_obj_file_types(filed_type))

        values = str(filed_value).strip('{}').split(SplitValueFiled)
        if not is_null_or_empty(values):
            for i in range(0,len(filed_types)):
                item_filed_type,item_filed_name = split_space(filed_types[i])
                v = values[i] if i < len(values) else ''

                self.record_filed(obj,item_filed_name,item_filed_type,v)
        else:
            log('record_obj_value is null:',filed_name)
        fill_value(parent,filed_name,obj)

    def add_filed(self,filed_name,filed_type,filed_des):
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
        self.build_filed(filed_name,filed_type,filed_des)

    def build_filed(self,filed_name,filed_type,filed_des,is_array = False):
        type_define = self.get_type_define(filed_type)
        if type_define == ETypeBase:
            proto_type = self.get_type_name(filed_type,filed_name)
            self.build_filed_proto(filed_name,proto_type,filed_des,is_array)
        elif type_define == ETypeList:
            self.build_list_filed(filed_name,filed_type,filed_des)
        elif type_define == ETypeObj:
            self.build_obj_filed(filed_name,filed_type,filed_des,is_array)

    def build_list_filed(self,filed_name,filed_type,filed_des):
        base_type,type_define = self.get_list_filed_info(filed_type)
        if type_define == ETypeBase:
            self.build_filed(filed_name,base_type,filed_des,True)
        elif type_define == ETypeObj:
            self.build_obj_filed(filed_name,base_type,filed_des,True)

    def get_list_filed_info(self,filed_type):
        base_type = filed_type[:-2]
        type_define = self.get_type_define(base_type)
        return base_type,type_define

    def build_obj_filed(self,filed_name,filed_type,filed_des,is_array = False):
        custom_msg = self.check_or_import_msg_type(filed_type)
        if custom_msg:
            self.build_filed_proto(filed_name,custom_msg.get_proto_name(),filed_des,is_array)
        else:
            class_name = first_char_upper(filed_name) + '_'
            msgItem = Message(class_name,'','',self,False)
            filed_types = get_obj_file_types(filed_type)
            for i in range(0,len(filed_types)):
                proto_filed_type,proto_filed_name = split_space(filed_types[i])
                msgItem.add_filed(proto_filed_name,proto_filed_type,proto_filed_name)
            msg = self.check_or_import_msg(msgItem)
            if msg:
                self.build_filed_proto(filed_name,msg.get_proto_name(),filed_des,is_array)
            else:
                self.build_filed_proto(filed_name,class_name,filed_des,is_array)
                self.child_msgs.append(msgItem)

    def check_or_import_msg_type(self,filed_type):
        custom_msg = self.try_get_global_msg(filed_type)
        if custom_msg:
            if not is_in_list(self.import_msgs,custom_msg.get_proto_name()):
                self.import_msgs.append(custom_msg.get_proto_name())
        return custom_msg

    def check_or_import_msg(self,msg):
        info = msg.get_class_info()
        for child in self.child_msgs:
            if child.get_class_info() == info:
                return child
        for global_msg in self.global_msgs:
            if global_msg.get_class_info() == info:
                import_name = global_msg.get_proto_name()
                if not is_in_list(self.import_msgs,import_name):
                    self.import_msgs.append(import_name)
                return global_msg
        return False

    def get_msg_file_types(self):
        fileds = []
        for filed in self.fileds_proto.values():
            fileds.append(filed)
        return fileds

    def build_filed_proto(self,filed_name,filed_type,filed_des,is_list):
        """
        构造message 文件内的字段
        :param filed_name: 字段名
        :param filed_type: 字段声明类型 （包含基础类型，数组，自定义对象等）
        :param filed_des:  字段描述 （即字段备注）
        :param is_list:    字段是否为数组
        :return:
        """
        filed = Filed(filed_name,filed_type,filed_des,is_list)
        self.fileds_proto[filed.get_filed_name()] = filed
        return filed

    def get_type_define(self,filed_type):
        """
        获取字段定义类型
        :param filed_type:
        :return: ETypeList ETypeObj or ETypeBase

        """
        if filed_type[-2:] == '[]':
            return ETypeList
        elif filed_type[0] == '{' and filed_type[-1] == '}':
            return ETypeObj
        elif BaseTypes.__contains__(filed_type):
            return ETypeBase
        elif self.try_get_global_msg(filed_type):
            return ETypeObj
        raise ValueError('unknown filed type:',filed_type)
        return ETypeObj

    def get_type_name(self,filed_type,file_name):
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
            return self.get_type_name(filed_type[:-2],file_name)
        elif define_type == ETypeBase:
            filed_type = filed_type.lower()
            return BaseTypes[filed_type]

class ProtoInfo:
    def __init__(self,msg,record_obj,is_single_sheet):
        self.message = msg
        self.record_obj = record_obj
        self.record_lower_obj = collections.OrderedDict()
        self.copy_obj(record_obj,self.record_lower_obj)
        self.is_single_sheet = is_single_sheet

    def copy_obj(self,source_obj,des_obj):
        for k, v in source_obj.items():
            self.record_obj_to_lower(k, v, des_obj)

    def record_obj_to_lower(self,key,value ,dest_obj):
        key = convert_to_lower_snake_cake(key)
        if isinstance(value, dict):
            dic_value = collections.OrderedDict()
            for k, v in value.items():
                self.record_obj_to_lower(k,v, dic_value)
            fill_value(dest_obj,key,dic_value)
        elif isinstance(value, list):
            list_value = []
            for i in range(len(value)):
                self.record_obj_to_lower(key,value[i],list_value)
            fill_value(dest_obj, key, list_value)
        else:
            fill_value(dest_obj, key, value)

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


class Filed:
    def __init__(self,filed_name,filed_type,filed_des,is_list = False):
        self.filed_name = filed_name
        self.filed_type = filed_type
        self.filed_des = filed_des.replace('\n','')
        self.is_list = is_list
        pass

    def get_name(self):
        return self.filed_name

    def get_filed_name(self):
        if self.is_list:
            return self.filed_name + 's'
        return self.filed_name

    def get_flat_buffer_filed_name(self):
        flat_filed_name = self.get_filed_name()
        flat_filed_name = convert_to_lower_snake_cake(flat_filed_name)
        return flat_filed_name


    def get_filed_type(self):
        return self.filed_type

    def get_defined_type(self):
        if self.is_list:
            return self.get_define_base_type() + '[]'
        return self.get_define_base_type()

    def get_define_base_type(self):
        if BaseProtoTypes.__contains__(self.filed_type):
            return BaseProtoTypes[self.filed_type]
        return self.filed_type

    def get_filed_des(self):
        return self.filed_des

    def get_define_proto(self,index):
        r = ''
        if self.is_list:
            r = ' repeated'
        return '%s %s %s = %s ; // %s' % (r,self.get_filed_type(),self.get_filed_name(),index,self.get_filed_des())

    def get_define_flat_scheme(self):
        """
        example v:[float:3];
        name:string;
        :param index:
        :return:
        """
        define_type = self.get_filed_type()
        if self.is_list:
            define_type =  "["+define_type+"]"
        return ' %s:%s ; // %s' % (self.get_flat_buffer_filed_name(),define_type,self.get_filed_des())

    def get_lua_api(self):
        r = ''
        if self.is_list:
            r = '[]'
        return '%s %s %s%s @%s ' % ("---@field ",self.get_filed_name(),self.get_filed_type(),r,self.get_filed_des())

    def scheme_info(self):
        return json.dumps((self.get_filed_name(),self.get_filed_type()),ensure_ascii = False,indent = 2)


def generator(file_list,out_protobuf_scripts,out_flatbuffer_scripts, out_data_formats,name_space,suffix):
    """

    :param file_list:  Excel Exports
    :param out_scripts:  Scripts Formats: Dictionary  key is protoc cmd, value is out folder
    :param out_data_formats: Export datas; key is lua json or protobuf, value is out folder
    :param name_space: Scripts NameSpace
    :param suffix: ScriptClass Suffix
    :return:
    """
    export = Exporter(file_list,out_protobuf_scripts,out_flatbuffer_scripts,out_data_formats,name_space,suffix)
    export.export()
