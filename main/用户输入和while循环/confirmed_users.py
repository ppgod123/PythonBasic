#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/13 15:11
 @功能模块:
 @模块备注:使用while循环来处理列表和字典
"""
unconfirmed_uesres=['andy','alice','bob','jackson','jhon','ben']
confirmed_uesres=[]
while unconfirmed_uesres:
    current_user=unconfirmed_uesres.pop()
    print ("认证用户:"+current_user.title())
    confirmed_uesres.append(current_user)
print("\n展示已经认证过的用户:")
for confirmed_ueser in confirmed_uesres:
    print (confirmed_ueser.title())
