#-*- coding: UTF-8 -*-
"""
 @编写人:冯爱军
 @开发时间:2022/1/25 14:43
 @功能模块:
 @模块备注:外星人入侵
"""
import sys
import pygame
import settings
from ship import Ship
import game_functions as gf

reload(sys)
sys.setdefaultencoding('utf-8')

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("外星人入侵！！！！")
    #设置背景色
    #bg_color = (230,230,230)
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #开始游戏的主循环
    while True:
        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #让最近绘制的屏幕可见
        pygame.display.flip()

def run_game2():
    pygame.display.set_caption("外星人入侵！！！！")
    #创建一艘飞船
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    #开始游戏主循环
    while True:
        #每次循环时都会重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

def run_game3():
    while True:
        ai_settings = settings.Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        ship = Ship(screen)
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)
if __name__ == '__main__':
    run_game3()