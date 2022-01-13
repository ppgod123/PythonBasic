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
prompt="根据您的姓名，可以获取确认您的相关权限。"
prompt+="\n请输入您的姓名:"
name=raw_input(prompt)
print("Hello,"+name+"!")