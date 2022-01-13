#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/13 14:36
 @功能模块:
 @模块备注:while循环
"""
# current_number=1
# while current_number<=10:
#     print (current_number)
#     current_number+=1
current_number=0
while current_number<10:
    # print (current_number)
    current_number+=1
    if current_number % 2 == 0:
        continue
    print (current_number)