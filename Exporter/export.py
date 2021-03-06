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
import os
import copyconfig

#要导出的配置文件
export_files = [
    '配置表1.xlsx',
    '配置表2.xlsx',
]

#导出的脚本和对应文件夹，key为protoc支持的， key is protoc cmd, value is out folder!
out_script_formats = {
    # 'python_out': 'out_python',
    'csharp_out': 'out_csharp',
    # 'cpp_out' : 'out_cpp',
    # 'java_out' : 'out_java'
}

#导出数据格式 ['json', 'lua', 'protobuf']
out_data_formats = {
    'json': 'out_json',
    'lua': 'out_lua',
    'protobuf': 'out_protobuf'
}

#拷贝到工程的路径
out_script_path = os.path.abspath(os.path.join(os.getcwd(), "../../../ClientMaster/Assets/Scripts/Config/"))
out_config_path = os.path.abspath(os.path.join(os.getcwd(), "../../../ClientMaster/Assets/Bundles/Config/"))

if __name__ == '__main__':
    tools.generator.generator(export_files,out_script_formats, out_data_formats, "Config", 'Template')
    # copyconfig.copy(out_data_formats, out_script_formats, out_config_path, out_script_path)
