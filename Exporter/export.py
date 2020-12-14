import tools.generator

export_files = [
    '全局配置表.xlsx',
    '任务配置表.xlsx',
    '英雄属性配置表.xlsx',
    'BUFF配置表.xlsx',
]

#key is protoc cmd, value is out folder!
ScriptTag_Dic = {
    'python_out': 'out_python',
    'csharp_out': 'out_csharp',
    'cpp_out' : 'out_cpp',
    'java_out' : 'out_java'
}

if __name__ == '__main__':
    tools.generator.generator(export_files,ScriptTag_Dic,"Config",'Template')
