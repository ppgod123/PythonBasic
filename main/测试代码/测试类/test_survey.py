#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/20 15:02
 @功能模块:
 @模块备注:
"""
import  unittest
import survey

class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonmyousSurvey类的测试"""
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        :return:
        """
        question = "你的母语是?"
        self.my_survey = survey.AnonymousSurvey(question)
        self.languages = ['英语','汉语','西班牙语','意大利语','俄语','德语']


    def test_store_single_response(self):
        """测试单个答案会被妥善存储"""
        # question = "你的母语是？"
        # my_survey = survey.AnonymousSurvey(question)
        self.my_survey.store_response(self.languages[0])
        self.assertIn(self.languages[0],self.my_survey.responses)
    def test_store_multiple_response(self):
        """测试多个答案会被妥善存储"""
        # question = "你的母语是？"
        # my_survey = survey.AnonymousSurvey(question)
        # languages = ['英语','俄语','西班牙语','法语','德语','泰语']
        for language in self.languages:
            self.my_survey.store_response(language)

        for language in self.languages:
            print(language)
            self.assertIn(language,self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()