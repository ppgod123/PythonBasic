#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/19 15:15
 @功能模块:
 @模块备注:
"""
import sys
filename = '999.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming!!!")
    file_object.write("\nI love create new games!!!")

print (sys.path)