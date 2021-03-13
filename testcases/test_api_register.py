import requests
import unittest
from ddt import ddt, data
from common.read_excel import ReadExcel

wb = ReadExcel('data/case001.xlsx', 'sheet1')
cases = wb.r_data_obj([1, 2, 3])


@ddt
class RegisterTestCase(unittest.TestCase):

    def __init__(self, methodName, case_obj):
        self.excepted = eval(case_obj.excepted)
        self.data = eval(case_obj.data)
        self.row = case_obj.case_id + 1
        super().__init__(methodName)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @data(*cases)
    def test_register(self, case):
        self.row = case.case_id + 1
        res = register(*eval(case.data))
        try:
            self.assertEqual(eval(case.excepted), res)
        except AssertionError as e:
            res = '失败'
            raise e
        else:
            res = 'pass'
        finally:
            wb.write_data(row=self.row, column=4, msg=res)


if __name__ == '__main__':
    unittest.main()