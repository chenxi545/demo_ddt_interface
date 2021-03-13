# 接口自动化测试框架之ddt数据驱动
本框架主要用python语言实现，以unittest单元测试为基础，采用ddt数据来驱动的，采用excel来管理测试用例。
## 项目框架说明
- common：自己封装的类存
   - config.py 封装读取配置文件的方法
   - constant.py 封装文件路径
   - do_mysql.py 封装操作mysql的方法
   - http_requests.py 封装接口发送请求的方法
   - logger.py 封装日志的方法
   - read_excel.py 封装读取excel用例的方法，**注意文件要ecxel文件仅支持.xlsx格式**
   - replace.py 封装正则方法，替换用例中的变量值
   - send_email.py 封装发送邮件方法
- conf:配置文件存放
   - config.ini 环境1配置文件
   - config1.ini 环境2配置文件
   - env.ini 环境切换开关
- librarys:别人封装的类存放
   - ddt.py 对ddt进行了细微调整，使
   - HTMLTestRunner_cn.py
- logs:日志存放
- data:测试用例数据存放 
- reports:测试报告存放 
- testcases:测试用例模块存放 
- run_suite.py 程序入口
## 使用说明
先拉取到本地，然后导入依赖包:

`pip install -r requirements.txt`

## 什么样的项目适合此框架
- 1.接口传入的参数字段少于20。
- 2.各接口相对独立，互相依赖性比较低。
- 3.适合比较简单的接口。

