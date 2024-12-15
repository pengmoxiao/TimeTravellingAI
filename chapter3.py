import pygame
import sys

# 初始化Pygame
pygame.init()

# 屏幕尺寸设置
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("维多利亚时代的伦敦")

# 加载大街图片、商店内部图片等资源（这里假设你已经有对应的图片文件）
street_image = pygame.transform.scale(pygame.image.load("street.png"),(screen_width,screen_height))
store_image = pygame.transform.scale(pygame.image.load("store.png"),(screen_width,screen_height))
rainy_street_image = pygame.transform.scale(pygame.image.load("rainy_street.png"),(screen_width,screen_height))
win_image = pygame.transform.scale(pygame.image.load("win.png"),(screen_width,screen_height))

# 一些用于游戏状态控制的变量
current_image = street_image
show_text = False
game_won = False
hidden1=False
hidden2=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos[0],event.pos[1])
            if current_image == street_image:
                # 点击人物显示文字的逻辑（这里简单示例，实际可能更复杂）
                if event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 100 and event.pos[1] < 200:
                    show_text = True
                # 点击商店的逻辑
                elif event.pos[0] > 300 and event.pos[0] < 400 and event.pos[1] > 300 and event.pos[1] < 400:
                    current_image = store_image
                    show_text = False
            elif current_image == store_image:
                # 点击遥控器的逻辑（这里简单示例，假设遥控器位置在某个范围）
                if event.pos[0] > 50 and event.pos[0] < 150 and event.pos[1] > 50 and event.pos[1] < 150:
                    current_image = rainy_street_image
            elif current_image == rainy_street_image:
                # 点击隐藏物品的计数逻辑（这里简单示例两个隐藏物品，实际需精确判断位置）
                #hidden_items_clicked = 0
                if event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 100 and event.pos[1] < 200:
                    #hidden_items_clicked += 1
                    hidden1=True
                    print(hidden1,hidden2)
                if event.pos[0] > 300 and event.pos[0] < 400 and event.pos[1] > 300 and event.pos[1] < 400:
                    hidden2=True
                    print(hidden1,hidden2)
                if hidden1 and hidden2:
                    game_won = True

    screen.blit(current_image, (0, 0))
    if show_text:
        font = pygame.font.Font("fonts/SimHei.ttf", 36)
        text = font.render("这里是一些初始文字提示", True, (255, 255, 255))
        screen.blit(text, (100, 100))
    if game_won:
        screen.blit(win_image, (0, 0))

    pygame.display.flip()