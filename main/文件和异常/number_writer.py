#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/19 19:39
 @功能模块:
 @模块备注:
"""
import json

numbers = [2,3,4,5,6,7,8,9,9527]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
