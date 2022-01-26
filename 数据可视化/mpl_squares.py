#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/26 14:59
 @功能模块:数据可视化
 @模块备注:
"""
import matplotlib
import matplotlib.pyplot as plt
import sys
from matplotlib import font_manager
from pylab import *
from matplotlib.font_manager import _rebuild
_rebuild()
reload(sys)
sys.setdefaultencoding('utf-8')
#使用matplotlib的字体管理器指定字体文件;fname指定字体文件  选简体显示中文
myfont = font_manager.FontProperties(fname="D:\Python27\Lib\site-packages\matplotlib\mpl-data\\fonts\\ttf\SimHei.ttf")

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']


squares = [1,4,5,13,7,16,25]
plt.plot(squares,linewidth = 2)
#设置图表标题，并给坐标轴加上标签
# plt.title("方块 数字", fontsize = 34,fontproperties=myfont)
# plt.xlabel("X轴值", fontsize = 14,fontproperties=myfont)
# plt.ylabel("Y轴值：", fontsize = 14,fontproperties=myfont)
plt.title("count统计",fontsize = 34,fontproperties=myfont)
plt.xlabel("X轴值", fontsize = 14,fontproperties=myfont)
plt.ylabel("Y轴值：", fontsize = 14,fontproperties=myfont)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 14)
plt.show()

print(matplotlib.matplotlib_fname())