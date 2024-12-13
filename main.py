import pygame
import sys

# 初始化
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("时间旅行解谜游戏")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 填充背景颜色
    screen.fill((0, 0, 0))  # 黑色背景

    # 更新显示
    pygame.display.flip()