#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/14 17:51
 @功能模块:
 @模块备注:
"""
import pizza
import Dog
from Dog import *
from Car import *
pizza.make_pizza(77,'里脊','','','')
#仅使用导入模块名，调用对应类、函数等需要加上模块名
# my_dog =Dog.Dog('哈士奇',4,'黑白色')
my_dog =Dog('哈士奇',4,'黑白色')
print ("My dog‘s name is "+my_dog.name)
print ("My dog‘s age is "+str(my_dog.age))
print ("My dog‘s color is "+my_dog.color)
my_dog.sit()
my_dog.roll_over()

my_car =Car('BMW','M5',2020)
print (my_car.get_car_info())