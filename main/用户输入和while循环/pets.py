#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/13 15:26
 @功能模块:
 @模块备注:删除包含特定值的所有列表元素
"""
pets = ['dog','cat','mouse','goldfish','rabbit','cat','pig','bear']
print(pets)
print(len(pets))
while 'cat' in pets:
    pets.remove('cat')
print(pets)
print(len(pets))
