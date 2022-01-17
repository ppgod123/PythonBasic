#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/14 19:11
 @功能模块:
 @模块备注:
"""
class Car(object):
  def __init__(self,make,model,year,odometer_reading):
      """初始化汽车属性"""
      self.make = make
      self.model = model
      self.year = year
      self.odometer_reading = odometer_reading
  def get_car_info(self):
      """获取汽车信息"""
      car_info=str(self.year)+' '+self.make+' '+self.model
      return car_info.upper()
  def read_odometer(self):
      """获取汽车信息"""
      car_info=str(self.odometer_reading)+'公里'
      return car_info.upper()
  def update_odometer(self,mileage):
      """将里程表读数设置为指定的值，禁止里程表读数往回调"""
      if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
      else:
         print ("里程表不可回调！！！")
  def increment_odometer(self,miles):
      """将里程表读数设置为指定的值，禁止里程表读数往回调"""
      if miles >= 0:
         self.odometer_reading += miles
      else:
         print ("增加里程数应为正整数！！！")
  def fill_gas_tank(self):
      """汽油车剩余油量"""
      print ("满油!!!")


