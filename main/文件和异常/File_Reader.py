#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/18 10:13
 @功能模块:
 @模块备注:
"""
import os
import sys

print os.getcwd()  #打印当前工作路径
print sys.path

# with open('cccc') as file_object:
#     contents = file_object.read()
#     print(contents)


path = 'C:\Users\Think\Desktop\PythonBasic\问题解决笔记.txt'
path = unicode(path,'utf-8') #经过编码处理
print(path)

with open(path) as file_object:
    contents = file_object.read()
    print(contents)