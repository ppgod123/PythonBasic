#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/12 16:58
 @功能模块:
 @模块备注:嵌套
"""
import random
# alien_0={'color':'green','points':5}
# alien_1={'color':'blue','points':5}
# alien_2={'color':'yellow','points':5}
# alien_3={'color':'red','points':5}
# alien_4={'color':'black','points':5}
#
# aliens=[alien_0,alien_1,alien_2,alien_3,alien_4]
# for alien in aliens:
#     print(alien)
#     print(random.randint(1,10000))

#创建一个用于存储外星人的空列表
aliens=[]
#颜色列表
colors=['red','yellow','green','orange','blue','white','gray','mauve']
#前闭后闭
print(colors[random.randint(0,7)])
#创建30个绿色的外星人
for alien_number in range(20):
    new_alien={'color':colors[random.randint(0,7)],'points':random.randint(1,999),'speed':'slow'}
    aliens.append(new_alien)
#修改部分字典信息
for alien in aliens[:5]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=666
for alien in aliens[-5:]:
    if alien['color']=='green':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=999
#显示前5个外星人
for alien in aliens[:6]:
    print(alien)
print('-----------------------------------------------------------------------')
#显示后5个外星人
for alien in aliens[-6:]:
    print(alien)
print('-----------------------------------------------------------------------')
#显示总共创建了多少个外星人
print('总共创建外星人数:'+str(len(aliens))+'人')