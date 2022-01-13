#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/13 15:38
 @功能模块:
 @模块备注:
"""
responses={}
polling_active = True

while polling_active:
    name=raw_input("\nWhat's your name? ")
    response = raw_input("Which mountain would you like to climb someday?")
    responses[name]=response
    repeat = raw_input("Would you like to let another person respond?(yes/no)")
    if repeat =='no':
        polling_active = False
print("\n----Poll Results----")
for name,response in responses.items():
    print(name+"想去爬"+response)