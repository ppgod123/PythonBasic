#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/19 15:30
 @功能模块:
 @模块备注:
"""

# try:
#     print (5/0)
# except ZeroDivisionError:
#     print ("5不可以除0！！！")
print ("填写两个数字，将进行除法计算")
print ("按q键退出")

while True:
    first_number = raw_input("\nFirst number:")
    if first_number =='q':
        break
    second_number = raw_input("Second number:")
    if second_number == 'q':
        break
    try:
        result = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print ('0不能作为除数')
    else:
        print (result)