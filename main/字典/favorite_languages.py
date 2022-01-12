#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/12 17:56
 @功能模块:
 @模块备注:字典中存储列表
"""
favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
  }
for name,languages in favorite_languages.items():
    if len(languages)==1:
     print("\n" + name.title() + "'s favorite language are:")
     for language in languages:
        print("\t"+language.title())
    else:
     print("\n"+name.title()+"'s favorite languages are:")
     for language in languages:
        print("\t"+language.title())