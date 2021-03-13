import os

# 获取项目目录的根目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 获取配置文件存放的目录路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# 日志保存的文件的目录路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# excel数据存放的目录路径
DATA_DIR = os.path.join(BASE_DIR, 'data')

# 测试用例存放的目录路径
CASE_DIR = os.path.join(BASE_DIR, 'testcases')

# 测试报告存放的目录路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')