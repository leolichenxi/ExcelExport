import logging
import hashlib
import copy
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置


def log(*args):
    logging.info("Info %s", args)


def is_null_or_empty(v):
    return v == '' or v is None


def get_bool_value(is_true):
    if is_true:
        return True
    return False


def is_in_list(in_list, value):
    for i in in_list:
        if i == value:
            return True
    return False


def find_index(key, v_list):
    for index, item in enumerate(v_list):
        if item == key:
            return index
    return -1


def get_file_md5(filename):
    if not os.path.isfile(filename):
        return
    my_hash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        my_hash.update(b)
    f.close()
    return my_hash.hexdigest()


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


def delete_empty_dic(obj):
    # dic = copy.deepcopy(obj)
    return obj


def is_base_type(obj):
    if isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, str) or isinstance(obj, bool):
        return True
    return False


def convert_to_lower_snake_cake(key):
    length = len(key)
    if length == 1:
        return key.lower()
    elif length >= 2:
        new_key = key[0].lower()
        for i in range(1, length):
            if key[i].isupper():
                new_key = new_key + "_" + key[i].lower()
            else:
                new_key = new_key + key[i]
            pass
        return new_key
    return key


def strip_filed(value):
    return str(value).strip()


def exists_file(file_path):
    return os.path.exists(file_path)
