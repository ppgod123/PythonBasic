#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/12 17:48
 @功能模块:
 @模块备注:字典中存储列表
"""
#存储所点披萨的信息
pizza={
    'crust':'trick',
    'toppings':['mushrooms','extra cheese']
    }
#概述所点的pizza
print("You ordered a"+pizza['crust']+"-crust pizza"+" with the following toppins:")
for topping in pizza['toppings']:
    print("\t"+topping)