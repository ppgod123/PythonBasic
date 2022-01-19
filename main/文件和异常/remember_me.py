#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/19 19:47
 @功能模块:
 @模块备注:
"""
import json

username = raw_input("请输入您的姓名：")
filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj,ensure_ascii=False)
    print("欢迎进入我们的系统:"+username+"!!!")