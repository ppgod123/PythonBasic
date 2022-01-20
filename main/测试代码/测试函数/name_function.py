#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/20 11:16
 @功能模块:
 @模块备注:
"""

def get_formatted_name(first,last):
    """组建完整姓名"""
    full_name = first+' '+last
    return full_name.title()
def get_formatted_name01(first,middle,last):
    """组建完整姓名"""
    full_name = first +' '+middle+' '+last
    return full_name.title()


if __name__ == '__main__':
    print (get_formatted_name('michael','•','jackson'))