#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/20 11:23
 @功能模块:
 @模块备注:
"""
import name_function
import unittest

print(name_function.get_formatted_name('michael','Jordan'))

print("按q键退出...")
while True:
    first = raw_input("\n 请输入姓:")
    if first =='q' or first =='Q':
       break
    last = raw_input("\n请输入名:")
    if last =='q' or last =='Q':
       break
    formatted_name = name_function.get_formatted_name(first,last)
    print ("全名:"+formatted_name)