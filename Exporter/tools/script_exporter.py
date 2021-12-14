import collections
import tools.utility as utility
import tools.lua_handler as lua_handler
import json
from google.protobuf.descriptor import FieldDescriptor as FD
import re
import string

## rools Define
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


def get_export_proto_folder():
    return OutDir_Protos


def handle_excel_str(value):
    v = str(value).replace('\\n', '\n')
    return v


def get_sheet_export_mark(sheet_name):
    """
    :param sheet_name:
    :return: sheet name
    """
    p = re.search('\|([a-zA-Z]\w+)', sheet_name)
    return p.group(1) if p else False


def get_global_sheet_info(sheet):
    """
    :param sheet:
    :return:
    """
    rows = sheet.row_values(0)
    name_index = utility.find_index(Global_Sheet_Tile[Index_Name], rows)
    type_index = utility.find_index(Global_Sheet_Tile[Index_Type], rows)
    value_index = utility.find_index(Global_Sheet_Tile[Index_Value], rows)
    rule_index = utility.find_index(Global_Sheet_Tile[Index_Rule], rows)
    des_index = utility.find_index(Global_Sheet_Tile[Index_Des], rows)
    if name_index == -1 or type_index == -1 or value_index == -1:
        return None
    return (name_index, type_index, value_index, rule_index, des_index)


def is_ignore_row(row):
    if len(row[0]) == 0:
        utility.log('empty row!', row)
        return True
    if len(row[0][0]) == 0:
        utility.log('empty row!', row)
        return True
    if row[0][0] == IgnoreSign:
        return True
    return False


def add_space_line(s, value):
    return '%s\n  %s' % (s, value)


def add_line(s, value):
    return '%s\n%s' % (s, value)


def fill_value(parent, filed_name, filed_value):
    if isinstance(parent, list):
        parent.append(filed_value)
    else:
        parent[filed_name] = filed_value


def convert(base_type, value, filed_name=None):
    if base_type == BaseTypeBool:
        bool_value = str(value)
        if bool_value in BooleanFalse:
            return utility.get_bool_value(False)
        elif bool_value in BooleanTrue:
            return utility.get_bool_value(True)
        else:
            raise ValueError("error!!!", base_type, filed_name, value)
    elif base_type == BaseTypeInt:
        if utility.is_null_or_empty(value):
            return 0
        value = int(float(value))
    elif base_type == BaseTypeFloat:
        if utility.is_null_or_empty(value):
            return 0
        value = float(value)
    elif base_type == BaseTypeDouble:
        if utility.is_null_or_empty(value):
            return 0
        value = float(value)
    elif base_type == BaseTypeString:
        if utility.is_null_or_empty(value):
            return ''
        value = handle_excel_str(value)
        value = str(value)
    else:
        raise ValueError("convert error! unknown type:", base_type, value, filed_name)
    return value


def get_type_define(filed_type, msg):
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
    elif msg.try_get_global_msg(filed_type):
        return ETypeObj
    raise ValueError('unknown filed type:', filed_type)
    return ETypeObj


def get_type_name(filed_type, file_name, msg):
    """
    获取字段类型名
    如果是对象，则直接为 file_name + '_'
    如果是list 则递归调用得到名字
    如果是基础字段 则直接返回 BaseTypes
    :param filed_type:
    :param file_name:
    :param msg:
    :return:
    """
    define_type = get_type_define(filed_type, msg)
    if define_type == ETypeObj:
        return file_name + '_'
    elif define_type == ETypeList:
        return get_type_name(filed_type[:-2], file_name, msg)
    elif define_type == ETypeBase:
        filed_type = filed_type.lower()
        return BaseTypes[filed_type]


def get_obj_file_types(filed_type):
    return filed_type.strip('{}').split(SplitObjArray)


def get_obj_value(filed_value):
    return re.findall(SplitArrayObjValue, str(filed_value))  ##--str(filed_value).strip('[]').split(SplitObjArray)


def split_space(s):
    return re.split(r'[' + string.whitespace + ']+', s.strip())


def build_lower_obj(source_obj):
    des_obj = collections.OrderedDict()
    for k, v in source_obj.items():
        record_obj_to_lower(k, v, des_obj)
    return des_obj


def get_list_values(filed_value):
    return str(filed_value).strip('[]').split(SplitArray)


def get_obj_list_values(filed_value):
    return str(filed_value).strip('{}').split(SplitValueFiled)


def record_obj_to_lower(key, value, dest_obj):
    key = utility.convert_to_lower_snake_cake(key)
    if isinstance(value, dict):
        dic_value = collections.OrderedDict()
        for k, v in value.items():
            record_obj_to_lower(k, v, dic_value)
        fill_value(dest_obj, key, dic_value)
    elif isinstance(value, list):
        list_value = []
        for i in range(len(value)):
            record_obj_to_lower(key, value[i], list_value)
        fill_value(dest_obj, key, list_value)
    else:
        fill_value(dest_obj, key, value)


def get_global_table_title(row, sheet_tile_info):
    filed_name = utility.strip_filed(row[sheet_tile_info[Index_Name]])
    filed_type = utility.strip_filed(row[sheet_tile_info[Index_Type]])
    filed_value = utility.strip_filed(row[sheet_tile_info[Index_Value]])
    filed_des = utility.strip_filed(row[sheet_tile_info[Index_Des]])
    filed_rule = utility.strip_filed(row[sheet_tile_info[Index_Rule]])
    return filed_name, filed_type, filed_value, filed_des, filed_rule


def get_list_table_title(sheet):
    row_des = sheet.row_values(Index_Item_Des)
    row_types = sheet.row_values(Index_Item_Type)
    row_names = sheet.row_values(Index_Item_Name)
    row_rules = sheet.row_values(Index_Item_Rule)
    return row_des, row_types, row_names, row_rules


def get_import_proto_define(msg_name):
    return 'import "%s/%s.proto";' % (get_export_proto_folder(), msg_name)


def get_json_data(data):
    obj = utility.delete_empty_dic(data)
    return json.dumps(obj, ensure_ascii=False, indent=2)


def get_lua_data(obj, lines=True):
    return lua_handler.get_lua_data(obj, 1, lines)


def get_proto_info_lua_list(info):
    return lua_handler.get_list_lua_script(info)


def dict2pb(cls, data_dict, strict=False):
    """
    Takes a class representing the ProtoBuf Message and fills it with data from
    the dict.
    """
    obj = cls()
    if data_dict is None:
        return obj
    for field in obj.DESCRIPTOR.fields:
        if not field.label == field.LABEL_REQUIRED:
            continue
        if not field.has_default_value:
            continue
        if not field.name in data_dict:
            raise ValueError('Field "%s" missing from descriptor dictionary.' % field.name)

    field_names = set([field.name for field in obj.DESCRIPTOR.fields])
    if strict:
        for key in data_dict.keys():
            if key not in field_names:
                raise ValueError('Key "%s" can not be mapped to field in %s class.' % (key, type(obj)))
    for field in obj.DESCRIPTOR.fields:
        if not data_dict.__contains__(field.name):
            continue
        msg_type = field.message_type
        if field.label == FD.LABEL_REPEATED:
            if field.type == FD.TYPE_MESSAGE:
                for sub_dict in data_dict[field.name]:
                    item = getattr(obj, field.name).add()
                    item.CopyFrom(dict2pb(msg_type._concrete_class, sub_dict))
            else:
                for i in data_dict[field.name]:
                    # map(getattr(obj, field.name).append, adict[field.name]) bug this function!
                    getattr(obj, field.name).append(i)
        else:
            if field.type == FD.TYPE_MESSAGE:
                value = dict2pb(msg_type._concrete_class, data_dict[field.name])
                getattr(obj, field.name).CopyFrom(value)
            else:
                try:
                    setattr(obj, field.name, data_dict[field.name])
                except Exception as e:
                    raise ValueError('setattr', field.type, field.name, data_dict[field.name], e)
    return obj
