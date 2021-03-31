
# 需要导出的excel 列表
export_files = [
    '英雄属性配置表.xlsx',
    'BUFF配置表.xlsx',
    '全局配置表.xlsx',
    '任务配置表.xlsx',
]

export_server_files = [
    '英雄属性配置表.xlsx',
]

export_format = "lua"          # json or lua or protobuf
export_out_folder = "client"    # 导出所在文件夹
export_client_sign = "client"
export_namespace = "Config"     # 脚本命名空间
export_suffix = "Template"      # 脚本尾缀
export_code_file = "code_dom.json"  # 脚本生成配置
export_json = 'export_config.json'  # 脚本生成描述
code_generator_path = "tools/CodeGenerator/CodeGenerator.exe"  # 脚本生成器路径

from tools import generator
import os
import sys
# import subprocess

def build_export_context(file_list,sign):
    """
    :param file_list: 导出的文件列表 list
    :param sign: 格式
    """
    result = {}
    result[generator.KeyFiles] = file_list
    result[generator.KeyFormat] = export_format
    result[generator.KeySign] = sign
    result[generator.KeyNameSpace] = export_namespace
    result[generator.KeySuffix] = export_suffix

    result[generator.KeyOutFolder] = export_out_folder
    result[generator.KeyCodeDom] = export_code_file
    result[generator.KeyExportJson] = export_json
    return result


def build_export_client():
    return build_export_context(export_files,export_client_sign)

def generate_code() :

    cmd = "start " + code_generator_path
    os.system(cmd)
    os.system('pause')
    # return
    # subprocess.Popen(code_generator_path)
    pass

def main():
    try:
        context = build_export_client( )
        generator.generate(context)
       # generate_code( )
        return 0
    except ExportError as e:
        print(e)
        return 1
    except Exception as e:
        print(e)
        traceback.print_exc()
        print("has error, see logs, please return key to exit")
        return 1

if __name__ == '__main__':
     sys.exit(main())

