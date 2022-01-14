#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/14 10:20
 @功能模块:
 @模块备注:
"""
import random
def greet_user():
    """显示简单问候语"""
    print('Hello World!!!')
greet_user()

def greet_user01(username):
    """显示简单问候语"""
    print('Hello World!!!'+username.title())
greet_user01('JAX'+str(random.randint(1,10)))
print ('-----------------------------------------------------------')
def get_formatted_name(first_name,last_name):
    """返回规范姓名"""
    full_name = first_name+' '+last_name
    return  full_name.title()
# 这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    f_name = raw_input("First name:")
    if f_name == 'q':
        break
    l_name = raw_input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello,"+formatted_name+"!")
