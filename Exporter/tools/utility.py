# coding:utf-8
import hashlib
import logging
from logging.handlers import RotatingFileHandler # 按文件大小滚动备份
import colorlog  # 控制台日志输入颜色
import time
import datetime
import os

cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)  # 如果不存在这个logs文件夹，就自动创建一个
logName = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d'))  # 文件的命名

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}

class Log:
    def __init__(self):
        self.logName = logName
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
            log_colors=log_colors_config)  # 日志输出格式
        self.handle_logs()

    def get_file_sorted(self, file_path):
        """最后修改时间顺序升序排列 os.path.getmtime()->获取文件最后修改时间"""
        dir_list = os.listdir(file_path)
        if not dir_list:
            return
        else:
            dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
            return dir_list

    def get_stamp_time(self, timestamp):
        """格式化时间"""
        time_struct = time.localtime(timestamp)
        return str(time.strftime('%Y-%m-%d', time_struct))

    def handle_logs(self):
        """处理日志过期天数和文件数量"""
        dir_log = 'logs' # 要删除文件的目录名
        dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\' + dir_log  #拼接删除目录完整路径
        file_list = self.get_file_sorted(dir_path)  # 返回按修改时间排序的文件list
        if file_list:  # 目录下没有日志文件
            for i in file_list:
                file_path = os.path.join(dir_path, i)  # 拼接文件的完整路径
                t_list = self.get_stamp_time(os.path.getctime(file_path)).split('-')
                now_list = self.get_stamp_time(time.time()).split('-')
                t = datetime.datetime(int(t_list[0]), int(t_list[1]),
                                      int(t_list[2]))  # 将时间转换成datetime.datetime 类型
                now = datetime.datetime(int(now_list[0]), int(now_list[1]), int(now_list[2]))
                if (now - t).days > 6:  # 创建时间大于6天的文件删除
                    self.delete_logs(file_path)
            if len(file_list) > 4:  # 限制目录下记录文件数量
                file_list = file_list[0:-4]
                for i in file_list:
                    file_path = os.path.join(dir_path, i)
                    print(file_path)
                    self.delete_logs(file_path)

    def delete_logs(self, file_path):
        try:
            os.remove(file_path)
        except PermissionError as e:
            self.warning('删除日志文件失败：{}'.format(e))

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = RotatingFileHandler(filename=self.logName, mode='a', maxBytes=1024 * 1024 * 5, backupCount=5,
                                 encoding='utf-8')  # 使用RotatingFileHandler类，滚动备份日志
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        ch = colorlog.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()  # 关闭打开的文件

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


CLog = Log()


def log(*args):
    CLog.debug(args)


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
