#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/14 16:24
 @功能模块:
 @模块备注:
"""
"""
创建一个字典，其中包含我们知道的有关用户的一切
"""
#字典使用**，列表使用*
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',location='princeton',field ='physics')
print (user_profile)
