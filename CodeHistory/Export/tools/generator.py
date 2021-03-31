#  表的名字和尾缀 作为className
#  表的字段对象

import string
import os
import sys
import re
import xlrd
import json
import codecs
import collections

KeyFiles = "files"
KeyFormat = "format"
KeySign = "exportSign"
KeyOutFolder = "outFolder"
KeyNameSpace = "namespace"
KeySuffix = "suffix"

KeyCodeDom = "code_dom"
KeyExportJson = "export_config"

KeyMembers = "elements"
KeyFiledName = "filedName"
KeyFiledType = "type"
KeyFiledComment = "comment"

KeySchemaFileName = 'export_file'
KeySchemaRoot = 'root'
KeySchemaItem = 'item'
KeySchemaSchema = 'schema'
# KeySchemaComment = 'comment'
KeyElementTypeName = "typeName"
KeyElementComment = "comment"

KeyIndexFiledName = 0
KeyIndexFiledType = 1
KeyIndexComment = 2
KeyIndexFormat = 3
SheetRowMaxSpaceCount = 3
SheetRowIgnore = "#"

ETypeList = "list"
ETypeObject = "obj"

EFormatJson = 'json'
EFormatLua = 'lua'
EFormatProto = 'proto'

KeyGlobalSheetTitles = ("name", "type", "value", "description")

BasicIntType = 'int'
BasicDoubleType = 'double'
BasicStringType = 'string'
BasicBoolType = 'bool'
BasicTypes = (BasicIntType, BasicDoubleType, BasicStringType, BasicBoolType)

def get_sheet_rows_index(row, name):
    """

    :param row: list
    :param name: key
    :return: index of key in list
    """
    for index, item in enumerate(row):
        if item == name:
            return index
    return -1
    pass


def get_export_filename(root, format, folder):
    filename = root + '.' + format
    filename = os.path.join(folder, filename)
    return filename


def get_main_info(typename, description):
    if isinstance(typename, BindType):
        typename = typename.type_name
    return [typename, description] if description else [typename]
    pass


def fill_value(parent, name, value, is_schema):
    if isinstance(parent, list):
        parent.append(value)
    else:
        if is_schema and not re.match('^_|[a-zA-Z]\w*$', name):
            raise ValueError('%s is a illegal identifier' % name)
        parent[name] = value
    pass


def split_space(s):
    return re.split(r'[' + string.whitespace + ']+', s.strip( ))


def get_bool(value):
    result = False
    try:
        value = int(float(value))
        result = False if value == 0 else True
    except ValueError:
        value = value.lower( )
        if value in ('false', 'no', 'off', 'n'):
            result = False
        elif value in ('true', 'yes', 'on', 'y'):
            result = True
            pass
        else:
            raise ValueError('%s is a illegal bool value' % value)
        pass
    return result


def newline(count):
    return '\n' + '  ' * count


class Record:
    def __init__(self, path, sheet, export_file, root, item, obj, export_mark):
        self.path = path
        self.sheet = sheet
        self.export_file = export_file
        self.root = root
        self.item = item
        self.set_object(obj)
        self.export_mark = export_mark

    def set_object(self, obj):
        self.schema = obj[0] if obj else None
        self.obj = obj[1] if obj else None
        pass


class BindType:
    def __init__(self, typename):
        self.type_name = typename

    def __eq__(self, other):
        return self.type_name == other


class Exporter:

    def __init__(self, context):
        self.context = context
        # self.context[KeyOutFolder] = os.path.abspath(self.context[KeyOutFolder])
        self.records = []
        pass

    pass

    def is_export_code(self):
        return self.context[KeyCodeDom] != None

    def check_path(self, path):
        result = next((result for result in self.records if result.path == path), False)
        if result:
            raise ValueError('%s is already export' % path)
        pass

    def check_sheet_name(self, path, sheet_name, root):
        result = next((result for result in self.records if result.root == root), False)
        if result:
            raise ValueError('%s in s% is already defined in s%,sheet name: s%' % (root, path, result.path, sheet_name))

    def get_export_mark(self, sheetName):
        """
        :param sheetName: 表名
        :return: 返回符合规则的表名
        """
        p = re.search('\|(_|[a-zA-Z]\w+)', sheetName)
        return p.group(1) if p else False

    def get_type_name(self, type):
        filed_type = type
        if type[-2] == "[" and type[-1] == "]":
            return ETypeList
        elif type[0] == "{" and type[-1] == "}":
            return ETypeObject
        elif type in BasicTypes:
            return type

        p = re.search('(int|string)[' + string.whitespace + ']*\((\S+)\.(\S+)\)', type)
        if p:
            return filed_type
        else:
            raise ValueError('%s is not a legal type ' % type)
        pass

    def build_list_express(self, parent, type, name, value, is_schema):
        base_type = type[:-2]
        list = []
        if is_schema:
            self.build_express(list, base_type, name, None, is_schema)
            list = get_main_info(list[0], value)
        else:
            values = value.strip('[]').split(',')
            for v in values:
                self.build_express(list, base_type, name, v, False)

        fill_value(parent, name + 's', list, is_schema)
        pass

    def build_obj_express(self, parent, type, name, value, is_schema):
        obj = collections.OrderedDict( )
        filed_name_types = type.strip('{}').split(':')
        if is_schema:
            for i in range(0, len(filed_name_types)):
                file_type, filed_name = split_space(filed_name_types[i])
                self.build_express(obj, file_type, filed_name, None, is_schema)
                pass
            obj = get_main_info(obj, value)
        else:
            filed_values = value.strip('{}').split(':')
            for i in range(0, len(filed_name_types)):
                if i < len(filed_values):
                    file_type, filed_name = split_space(filed_name_types[i])
                    self.build_express(obj, file_type, filed_name, filed_values[i], False)
                pass
        fill_value(parent, name, obj, is_schema)
        pass

    def build_base_express(self, parent, type, name, value, is_schema):
        type_name = self.get_type_name(type)
        if is_schema:
            value = get_main_info(type_name, value)
        else:
            if False and type_name != BasicStringType:
                return
            elif type_name == BasicDoubleType:
                value = float(value)
            elif type_name == BasicStringType:
                value = str(value)
            elif type_name == BasicIntType:
                value = int(float(value))
            elif type_name == BasicBoolType:
                value = get_bool(value)
            pass
        fill_value(parent, name, value, is_schema)
        if not is_schema and isinstance(type_name, BindType):
            print(" TODO ***********")
            print(type_name.mark)
        pass

    def build_express(self, parent, type, name, value, is_schema):
        type_name = self.get_type_name(type)
        if type_name == ETypeList:
            self.build_list_express(parent, type, name, value, is_schema)
            pass
        elif type_name == ETypeObject:
            self.build_obj_express(parent, type, name, value, is_schema)
            pass
        else:
            self.build_base_express(parent, type, name, value, is_schema)
            pass
        pass

    def get_sheet_info(self, sheet):
        """
        :param sheet: 单表
        :return: 元组 title info   none means a global config sheet
        """
        rows = sheet.row_values(0)
        index_name = get_sheet_rows_index(rows, KeyGlobalSheetTitles[0])
        index_type = get_sheet_rows_index(rows, KeyGlobalSheetTitles[1])
        index_value = get_sheet_rows_index(rows, KeyGlobalSheetTitles[2])
        index_des = get_sheet_rows_index(rows, KeyGlobalSheetTitles[3])

        if index_name == -1 or index_type == -1 or index_value == -1:
            return None
        return (index_name, index_type, index_value, index_des)

    def export_item_sheet(self, sheet):
        descriptions = sheet.row_values(0)
        types = sheet.row_values(1)
        names = sheet.row_values(2)
        signs = sheet.row_values(3)
        title_infos = []
        schema_obj = collections.OrderedDict( )
        try:
            for col_index in range(sheet.ncols):
                type = str(types[col_index]).strip( )
                name = str(names[col_index]).strip( )
                sign = str(signs[col_index]).strip( )
                title_infos.append((type, name, sign))
                if self.is_export_code( ):
                    if type and name and sign:
                        self.build_express(schema_obj, type, name, descriptions[col_index], True)
            pass
        except Exception as e:
            raise e
            pass
        list = []
        has_export = next((i for i in title_infos if i[0] and i[1] and i[2]), False)
        if has_export:
            try:
                space_row_count = 0
                for row_index in range(4, sheet.nrows):
                    row = sheet.row_values(row_index)
                    item = collections.OrderedDict( )
                    first_text = str(row[0]).strip( )
                    if not first_text:
                        space_row_count += 1
                        if space_row_count >= SheetRowMaxSpaceCount:
                            break
                    if not first_text or first_text[0] == SheetRowIgnore:  #
                        continue
                    for col_index in range(sheet.ncols):
                        type = title_infos[col_index][0]
                        name = title_infos[col_index][1]
                        value = str(row[col_index])
                        if type and name and value:
                            self.build_express(item, type, name, value, False)
                    space_row_count = 0
                    if item:
                        list.append(item)
            except Exception as e:
                raise e
        return (schema_obj, list)

    def export_global_sheet(self, sheet, titles):
        # (index_name, index_type, index_value, index_des)
        index_name = titles[0]
        index_type = titles[1]
        index_value = titles[2]
        index_des = titles[3]

        schema_obj = collections.OrderedDict( )
        export_obj = collections.OrderedDict( )

        try:
            space_row_count = 0
            for row_index in range(1, sheet.nrows):
                row = sheet.row_values(row_index)
                name = str(row[index_name]).strip( )
                type = str(row[index_type]).strip( )
                value = str(row[index_value]).strip( )
                des = str(row[index_des]).strip( )
                if not name and not value and not type:
                    space_row_count += 1
                    if space_row_count >= SheetRowMaxSpaceCount:
                        break
                    continue
                if name and type:
                    if (name[0] != SheetRowIgnore):
                        self.build_express(schema_obj, type, name, des, True)
                        if value:
                            self.build_express(export_obj, type, name, value, False)
                space_row_count = 0
        except Exception as e:
            raise e
        return (schema_obj, export_obj)

    def get_root_name(self, export_mark, is_sheet_title):
        root = export_mark + 's' + self.context[KeySuffix]
        item = export_mark
        if is_sheet_title:
            root = export_mark + self.context[KeySuffix]
            item = None
        return root, item

    def add_record(self, path, sheet, export_file, root, item, export_object, export_mark):
        r = Record(path, sheet, export_file, root, item, export_object, export_mark)
        self.records.append(r)
        pass

    def check_constraint(self):
        pass

    def save_json(self, record):
        json_str = json.dumps(record.obj, ensure_ascii=False, indent=2)
        with codecs.open(record.export_file, 'w', 'utf-8') as f:
            f.write(json_str)
        print('Export: %s from %s in %s' % (record.export_file, record.sheet.name, record.path))
        pass

    def to_lua(self,obj,indent = 1):
        if isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, str):
            yield json.dumps(obj, ensure_ascii = False)
        else:
            yield '{'
            is_list = isinstance(obj,list)
            is_first = True

            for i in obj:
                if is_first :
                    is_first = False
                else :
                    yield ','
                yield newline(indent)
                if not is_list :
                    k = i
                    i = obj[k]
                    yield k
                    yield ' = '
                for part in self.to_lua(i, indent + 1):
                    yield part

            yield newline(indent - 1)
            yield '}'

    def save_lua(self,record):
        lua_str = "".join(self.to_lua(record.obj))
        with codecs.open(record.export_file, 'w', 'utf-8') as f:
            f.write('return ')
            f.write(lua_str)
        print('Export: %s from %s in %s' % (record.export_file, record.sheet.name, record.path))
        pass

    def save_protobuf(self, record):
        json_str = json.dumps(record.obj, ensure_ascii=False, indent=2)
        with codecs.open(record.export_file, 'w', 'utf-8') as f:
            f.write(json_str)
        print('Export: %s from %s in %s' % (record.export_file, record.sheet.name, record.path))
        pass

    def save(self, record):
        if not record.obj:
            return
        if not os.path.isdir(self.context[KeyOutFolder]):
            os.makedirs(self.context[KeyOutFolder])

        if self.context[KeyFormat] == EFormatJson:
            self.save_json(record)
            pass
        elif self.context[KeyFormat] == EFormatLua:
            self.save_lua(record)
            pass
        elif self.context[KeyFormat] == EFormatProto:
            self.save_protobuf(record)
            pass
        pass

    def saves(self):
        schemas = []
        for record in self.records:
            self.save(record)
            if self.is_export_code( ):
                schemas.append(
                    {
                        KeySchemaFileName: record.export_file,
                        KeySchemaRoot: record.root,
                        KeySchemaItem: record.item or record.export_mark,
                        KeySchemaSchema: record.schema
                    }
                )
        if schemas and self.is_export_code( ):
            schema_json = json.dumps(schemas, ensure_ascii=False, indent=2)
            dir = os.path.dirname(self.context[KeyCodeDom])
            if dir and not os.path.isdir(dir):
                os.makedirs(dir)
            with codecs.open(self.context[KeyCodeDom], 'w', 'utf-8') as f:
                f.write(schema_json)

    def export(self):
        file_paths = self.context[KeyFiles]
        for path in file_paths:
            if not path:
                continue
            self.check_path(path)
            # print(path)
            excel_data = xlrd.open_workbook(path)
            count = None
            for sheet in excel_data.sheets( ):
                export_mark = self.get_export_mark(sheet.name)
                if export_mark:
                    sheet_title_info = self.get_sheet_info(sheet)
                    root, item = self.get_root_name(export_mark, sheet_title_info)
                    export_filepath = get_export_filename(root, self.context[KeyFormat], self.context[KeyOutFolder])
                    self.check_sheet_name(path, sheet.name, root)
                    export_obj = None
                    if item:
                        export_obj = self.export_item_sheet(sheet)
                    else:
                        export_obj = self.export_global_sheet(sheet, sheet_title_info)
                    self.add_record(path, sheet, export_filepath, root, item, export_obj, export_mark)
                pass

        self.check_constraint( )
        self.saves( )
        pass

    def debug(self):
        print(self.context)
        pass


def export_excel(context):
    """
     :param context: 导出的文件列表 Dictionary
     """
    exporter = Exporter(context)
    exporter.export()
    export_json = json.dumps(context, ensure_ascii=False, indent=2)
    dir = os.path.dirname(context[KeyCodeDom])
    if dir and not os.path.isdir(dir):
        os.makedirs(dir)
    with codecs.open(context[KeyExportJson], 'w', 'utf-8') as f:
        f.write(export_json)
    print("export finish!!!")
    pass


def generate(context):
    export_excel(context)
    pass
