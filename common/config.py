import configparser
import os
from common.constant import CONF_DIR

class ReadConfig(configparser.Configparser):

    def __init__(self):
        super().__init__()
        self.read(os.path.join(CON_DIR,'config.ini'),encoding='utf-8')

conf = ReadConfig()

if __name__ == '__main__':
    res = conf.get('excel','file_name')
    print(res)