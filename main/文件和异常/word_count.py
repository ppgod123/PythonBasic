#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/19 19:03
 @功能模块:
 @模块备注:统计文件中词汇量方法
"""
def count_words(filename):
    """计算一个文件包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except IOError:
        msg = "所读取文件名："+filename+",该文件不存在!!!"
        print (msg)
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print ("所读取文件名："+filename+",该文件内容共计"+str(num_words)+"字")

if __name__ == '__main__':
    filename = '999.txt'
    count_words(filename)
filenames = ['888.txt','999.txt','a.txt','cccc','777']
for filename in filenames:
    count_words(filename)