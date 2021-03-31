import os
import shutil

copyType = ".json"
bundlesName = "Bundles/Config"
formPath = os.getcwd() + "/client/"
targetPath = os.path.abspath(os.path.join(os.getcwd(), "../../../ClientMaster/Assets/Scripts/Config/"))
jsonTargetPath = os.path.abspath(os.path.join(os.getcwd(), "../../../ClientMaster/Assets/Bundles/Config/"))


def copy_dir(from_file, to_file, to_json_file):
    if not os.path.exists(to_file):  # 如不存在目标目录则创建
        os.makedirs(to_file)
    if not os.path.exists(to_json_file) and not os.path.exists(jsonTargetPath):
        os.makedirs(to_json_file)
    files = os.listdir(from_file)  # 获取文件夹中文件和目录列表
    for f in files:
        if os.path.isdir(from_file + '/' + f):  # 判断是否是文件夹
            copy_dir(from_file + '/' + f, to_file + '/' + f, to_json_file + '/' + f)  # 递归调用本函数
        else:
            if f.endswith(copyType):
                shutil.copy(from_file + '/' + f, to_json_file + '/' + f)  # 拷贝Json文件
            else:
                shutil.copy(from_file + '/' + f, to_file + '/' + f)  # 拷贝Class文件


if __name__ == '__main__':
    copy_dir(formPath, targetPath, jsonTargetPath)
