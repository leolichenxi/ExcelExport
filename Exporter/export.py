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

import tools.generator

export_files = [
    '全局配置表.xlsx',
    '任务配置表.xlsx',
    '英雄属性配置表.xlsx',
    'BUFF配置表.xlsx',
]



#key is protoc cmd, value is out folder!
ScriptTag_Dic = {
    # 'python_out': 'out_python',
    'csharp_out': 'out_csharp',
    # 'cpp_out' : 'out_cpp',
    # 'java_out' : 'out_java'
}

# ['json', 'lua', 'protobuf']
out_data_formats = ['json', 'lua', 'protobuf']

if __name__ == '__main__':
    tools.generator.generator(export_files,ScriptTag_Dic, out_data_formats, "Config", 'Template')
