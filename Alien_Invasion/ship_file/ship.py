#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/25 16:23
 @功能模块:
 @模块备注:
"""
import pygame

class Ship():
    def __init__(self,screen):
        """初始化飞船并设置其初始未知"""
        self.screen = screen
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship_file.jpg')
        self.rect = self.image.get_rect()
        self.screen_resct = screen.get_rect()

        #将每艘新飞机放在屏幕底部中央
        self.rect.centerx = self.screen_resct.centerx
        self.rect.bottom = self.screen_resct.bottom
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)