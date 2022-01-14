#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/14 15:16
 @功能模块:
 @模块备注:
"""
# def formatted_name(first_name,last_name):
#     """返回格式姓名"""
#     full_name =first_name+' '+last_name
#     return full_name.title()
# Name=formatted_name('micheal','jackson')
# print (Name)
# print('==========================================================')
def formatted_name(first_name,middle_name,last_name):
    """返回格式姓名"""
    if middle_name:
       full_name =first_name+' '+middle_name+' '+last_name
    else:
       full_name = first_name + ' ' + last_name
    return full_name.title()
Name1=formatted_name('micheal','m','jackson')
print (Name1)
Name2=formatted_name('bruce','','lee')
print (Name2)