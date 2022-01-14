#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/14 18:41
 @功能模块:
 @模块备注:
"""

class Dog():
    """创建小狗类的简单尝试"""
    def __init__(self,name,age,color):
        """初始化属性"""
        self.name = name
        self.age = age
        self.color = color
    def sit(self):
        """模拟小狗被命令是蹲下"""
        print(self.name.title()+" is now sitting")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print (self.name.title()+" rolled over!")

if __name__ == '__main__':
    my_dog=Dog('bomei',3,'yellow')
    print ("My dog‘s name is "+my_dog.name)
    print ("My dog‘s age is "+str(my_dog.age))
    print ("My dog‘s color is "+my_dog.color)
    my_dog.sit()
    my_dog.roll_over()