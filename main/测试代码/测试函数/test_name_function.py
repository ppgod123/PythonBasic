#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/20 11:56
 @功能模块:
 @模块备注:
"""
import name_function
import unittest
class NameTestCase(unittest.TestCase):
    """测试姓名函数"""
    def test_first_middle_last_name(self):
        formatted_name = name_function.get_formatted_name01('michael','•','jackson')
        self.assertEqual(formatted_name,'Michael • Jackson')
    def test_first_last_name(self):
        formatted_name = name_function.get_formatted_name('michael','jackson')
        self.assertEqual(formatted_name,'Michael Jackson')

if __name__ == '__main__':
    unittest.main