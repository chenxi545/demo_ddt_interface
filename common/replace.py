import re
from common.config import conf

class ConText:
    # 用来存储临时变量
    loan_id = None


def replace(data):
    """
    用例参数化替换
    :param data:
    :return:
    """
    # 正则表达式，替换##包括的内容，替换的内容从配置文件中获取
    p = r'#(.+?)#'
    # 判断该用例参数是否有需要替换的
    while re.search(p,data):
        # 去用例中获取需要替换的变量名
        key = re.search(p,data).group(1)
        try:
            # 去配置文件获取需要替换变量的值
            value = conf.get('test_data',key)
        except:
            # 获取用例执行的时候，存在类里的临时数据
            value = getattr(ConText,key)
        # 进行替换
        data = re.sub(p,value,data,count=1)
    return data


if __name__ == '__main__':

    # data = '{"user":"#user#","password":"#password#"}'
    # data = replace(data)
    # print(data)

    # 设置类属性
    setattr(ConText,'name','madong')
    # 获取类属性
    name = getattr(ConText,'name')
    print(name)