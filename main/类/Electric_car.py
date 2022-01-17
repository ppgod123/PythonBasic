#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/17 17:25
 @功能模块:
 @模块备注:
"""
from Car import Car

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year,odometer_reading):
        """初始化父类的属性"""
        super(ElectricCar,self).__init__(make,model,year,odometer_reading)
        self.battery_size = 700
        self.battery = battery()

    def describle_battery(self):
        """打印一条描述电瓶容量的消息"""
        print ("This car has a "+str(self.battery_size)+"-kWh battery.")

    def fill_gas_tank(self):
        """汽油车剩余油量"""
        print ("无需加油!!!")
class battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print ("这辆车拥有"+str(self.battery_size)+"-kwh 电池容量")
    def get_range(self):
        """根据不同电池容量，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range =240
        elif self.battery_size == 85:
            range = 270
        message = "这辆车最大行驶里程为:"+str(range)
        message += "公里，满电情况下"
        print (message)

if __name__ == '__main__':
    my_tesla = ElectricCar('telsa','model s',2020,10000)
    print (my_tesla.odometer_reading)
    print (my_tesla.get_car_info())
    my_tesla.describle_battery()
    my_tesla.fill_gas_tank()
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    my_car = Car('byd','汉',2022,9527)
    print (my_car.get_car_info())
    print (my_car.read_odometer())
    print (my_car.odometer_reading)
    my_car.fill_gas_tank()