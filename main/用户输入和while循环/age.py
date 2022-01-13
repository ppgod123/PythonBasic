#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/13 10:15
 @功能模块:
 @模块备注:
"""
"""
python2需要使用raw_input函数，python3支持input函数
"""
age=input("根据您的姓名，可以获取确认您的相关投票权限。"+"\n请输入您的年龄:")
if age<=18:
    print(str(age)+"岁"+",you are too young to vote !!!")
else:
    print(str(age)+"岁"+",you are old enough to vote!!!")