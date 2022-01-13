#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/13 10:15
 @功能模块:
 @模块备注:
"""
#python2需要使用raw_input函数，python3支持input函数
Tip=("告诉我你想要操作的内容，我将提供相关内容给您")
Tip+=("\n点击’quit‘终止程序运行:")
message=""
active = True
while active:
    message = raw_input(Tip)
    if message =='quit':
       break
    else:
       print("我喜欢"+message.title()+"!")

