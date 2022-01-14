#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/14 14:25
 @功能模块:
 @模块备注:
"""
pets={
   'dog':'bob',
   'cat':'andy',
   'mouse':'kiki',
   'goldfish':'haha',
   'pig':'jhon',
  }
def describe_pet(animal_type,pet_name='777'):
    """显示宠物信息"""
    print("I have an "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('dargon')
describe_pet("dog","bob")
describe_pet(animal_type='dargon')
describe_pet(pet_name="Jax",animal_type="tiger")


for animal_type,pet_name in pets.items():
    describe_pet(animal_type, pet_name)