#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/12 18:09
 @功能模块:
 @模块备注:字典中存储字典
"""
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princetom'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

for username,user_info in users.items():
    print("\nUsername:"+username)
    full_name = user_info['first']+" "+user_info['last']
    location=user_info['location']
    print('\tFullName:'+full_name.title())
    print('\tLocation:'+ location.title())