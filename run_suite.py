import unittest, os, time
from common.constant import REPORT_DIR, CASE_DIR
from common.config import conf
from librarys.HTMLTestRunner_cn import HTMLTestRunner
from common.send_email import send_email_file

file_name = conf.get('report', 'filename')
filename = file_name + time.strftime("%Y%m%d%H%M%S", time.localtime())
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))
filepath = os.path.join(REPORT_DIR, filename)
with open(filepath, 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='report',
        description='测试报告',
        tester='madong'
    )
    runner.run(suite)

# 发送测试报告到邮箱
send_email_file(filepath)
