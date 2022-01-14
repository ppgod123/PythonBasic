#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/14 19:11
 @功能模块:
 @模块备注:
"""
class Car():
  def __init__(self,make,model,year):
      """初始化汽车属性"""
      self.make = make
      self.model=model
      self.year=year

  def get_car_info(self):
      """获取汽车信息"""
      car_info=str(self.year)+' '+self.make+' '+self.model
      return car_info.upper()
  