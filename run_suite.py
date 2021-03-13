import unittest
from HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.discover(r'/Users/madong/PycharmProjects/pythonProject/testcases'))
with open('reports/reports.html','wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='report',
        description='测试报告',
        tester='madong'
    )
    runner.run(suite)