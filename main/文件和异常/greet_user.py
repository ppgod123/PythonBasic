#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/19 19:59
 @功能模块:
 @模块备注:
"""
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("欢迎归来！"+ username + "!")