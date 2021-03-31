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

import os
import shutil

def copy_dir(from_file, to_file):
    # root 文件夹下的所有文件夹（包括子文件夹）的路径名字../data/20170308/221.176.64.146\1
    # dirs 返回文件夹下面所有文件（包括子文件夹）的文件夹名字数组['1', '2', '3', '4', '5', '6', '7']
    # files 返回文件夹线面所有文件（包括子文件夹）的文件名字数组['newdata.json', 'transformtxt.json']
    # files = os.listdir(from_file)  # 获取文件夹中文件和目录列表
    for root, dirs, files in os.walk(from_file):
        for f in files:
            # 判断是否是文件夹
            if os.path.isdir(from_file + '/' + f):
                # 递归调用本函数
                copy_dir(from_file + '/' + f, to_file + '/' + f)
            else:
                out_path = to_file + '/' + os.path.basename(root)
                # 如不存在目标目录则创建
                if not os.path.exists(out_path):
                    os.makedirs(out_path)
                #拷贝
                shutil.copy(from_file + '/' + f, out_path + '/' + f)  # 拷贝\文件


def copy(config_files, script_files, out_config_path, out_script_path):
    # 拷贝脚本文件
    for k, v in script_files.items():
        copy_dir(os.getcwd() + '/' + v, out_script_path)
    # 拷贝配置文件
    for k, file in config_files.items():
        copy_dir(os.getcwd() + '/' + file, out_config_path)
