#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/18 11:18
 @功能模块:
 @模块备注:使用文件的内容
"""
filename = 'a.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string +=line.strip()

print(pi_string[:9]+'...')
print(len(pi_string))