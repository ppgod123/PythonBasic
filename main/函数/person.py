#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/14 15:40
 @功能模块:
 @模块备注:
"""
def build_person(first_name,last_name,age=''):
    """返回一个字典，包含人的信息"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
person=build_person('micheal','jakcson',age=27)
print(person)