#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/20 14:29
 @功能模块:
 @模块备注:
"""
import survey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "你的母语是？"
my_survey = survey.AnonymousSurvey(question)

#显示问题并存储答案
my_survey.show_question()
print("按q键退出\n")
while True:
    response = raw_input("语言:")
    if response =='Q' or response =='q':
        break
    my_survey.store_response(response)

#显示调查结果
print("\n非常感谢您参与此次问卷调查！！！")
my_survey.show_results()
