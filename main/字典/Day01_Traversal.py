#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/12 13:58
 @功能模块:
 @模块备注:遍历
"""
alien_0={'color':'green','points':5}
friends=['Andy','Ben']
favorite_languages={
    'Andy':'Java',
    'Bob':'C',
    'Bill':'PHP',
    'Ben':'Python',
    'tiger':'C',
    'Alice':'C++',
    'Amy':'Java'
  }
# 遍历所有键
for key in favorite_languages:
     print('\nkey:'+key)
    # print('\n')
# 遍历所有键值
for name,language in favorite_languages.items():
    print('\nkey:'+name.upper())
    print('value:'+language.upper())
    if name in friends:
        print("Hi,"+name.upper()+",I see your favorite language is"+favorite_languages[name].upper()+"!")
for name in sorted(favorite_languages.keys()):
    print (name.upper()+",终于找到你啦!")
# 遍历所有值
for language in favorite_languages.values():
    print(language.upper())
# 遍历所有值去重
for language in set(favorite_languages.values()):
    print(language.upper())