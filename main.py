import pygame
import sys

# 初始化
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("时间旅行解谜游戏")

# 加载中文字体文件（这里假设字体文件在项目目录下名为SimHei.ttf）
font = pygame.font.Font("SimHei.ttf", 36)

# 渲染中文游戏标题文本
title_text = font.render("时间旅行解谜", True, (255, 255, 255))
title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 3))

# 渲染中文开始游戏提示文本
start_text = font.render("按任意键开始游戏", True, (255, 255, 255))
start_rect = start_text.get_rect(center=(screen_width // 2, screen_height // 2))

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 这里后续可以添加按下按键后进入游戏具体逻辑的代码，比如加载游戏关卡等
            print("开始游戏啦，后续可添加具体逻辑")

    screen.fill((0, 0, 0))
    # 在屏幕上绘制游戏标题
    screen.blit(title_text, title_rect)
    # 在屏幕上绘制开始游戏提示
    screen.blit(start_text, start_rect)

    # 更新显示
    pygame.display.flip()