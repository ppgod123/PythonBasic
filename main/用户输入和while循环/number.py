#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/13 10:15
 @功能模块:
 @模块备注:求模运算符
"""
"""
python2字符串需要使用raw_input函数，input函数只支持数字，python3支持input函数
"""
number=input("根据您填写的数字判断奇偶。"+"\n请输入您的数字:")
number=int(number)
if number % 2 == 0:
    print("数字"+str(number)+"是偶数！")
else:
    print("数字" + str(number) + "是奇数！")