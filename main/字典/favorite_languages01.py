#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/12 17:56
 @功能模块:
 @模块备注:字典中存储列表
"""
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['ben'] = 'go'
favorite_languages['jhon'] = 'java'
favorite_languages['hook'] = 'c++'

for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+" !!!")