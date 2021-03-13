import logging
from common.config import conf

# 读取配置文件相关参数
logger_name = conf.get('logs', 'logger_name')
lever = conf.get('logs', 'lever').upper
sh_lever = conf.get('logs', 'sh_lever').upper
fh_lever = conf.get('logs', 'fh_lever').upper
log_file_path = conf.get('logs', 'log_file_path')


class MYLogging(object):
    """自定义日志类"""

    def __new__(cls, *args, **kwargs):
        # 创建自己的日志收集器
        my_log = logging.getLogger(logger_name)
        my_log.setLevel(lever)
        # 创建一个日志输出渠道
        l_s = logging.StreamHandler()
        l_s.setLevel(sh_lever)
        # 将日志输出渠添加到日志收集器中
        l_f = logging.FileHandler(log_file_path, encoding='utf8')
        l_f.setLevel(fh_lever)
        # 设置日志输出格式
        ft = '%(asctime)s - [%(filename)s --> line:%(lineno)d] - %(levelname)s: %(message)s'
        ft = logging.FileHandler(ft)
        l_s.setFormatter(ft)
        l_f.setFormatter(ft)


logger = MYLogging()
