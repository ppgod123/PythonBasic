#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/17 18:29
 @功能模块:
 @模块备注:
"""
from random import randint
class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    def roll_die(self):
        x = randint(1,6)
        print(x)
    def roll_die01(self):
        x = randint(1,10)
        print(x)
    def roll_die02(self):
        x = randint(1,20)
        print(x)

if __name__ == '__main__':
    for i in range(0,10,1):
        Die().roll_die()
    print ("------------------------------")
    for i in range(0,10,1):
        Die().roll_die01()
    print ("------------------------------")
    for i in range(0,10,1):
        Die().roll_die02()
