
#1. 表头生成Proto
#
#

NAME_SPACE = 'Config'
SUFFIX = 'Template'
SYNTAX = 'proto3'
MESSSAGE_NAME = 'message'
TAB_SPACE = '  '
TAB_LINE = '\n'

import xlrd

def get_sheet_info(sheet):
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
