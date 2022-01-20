#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/19 19:47
 @功能模块:
 @模块备注:
"""
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# username = raw_input("请输入您的姓名：")
# filename = 'username.json'
# with open(filename,'w') as f_obj:
#     json.dump(username,f_obj,ensure_ascii=False)
#     print("欢迎进入我们的系统:"+username+"!!!")

#重构
def greet_user():
    """问候用户并指出其名字"""
    filename = 'username.json'
    try:
     with open(filename) as f_obj:
         username = json.load(f_obj)
    except IOError:
        username = raw_input("Q亲输入您的姓名:")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj,ensure_ascii=False)
            print("我们将记住你！！！"+username)
    else:
        print ("欢迎归来，"+username +"!")

def get_stored_username():
    """若存储了用户，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = raw_input("请输入您的姓名:")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username


if __name__ == '__main__':
    greet_user()
    print (get_stored_username())
    print (get_new_username())