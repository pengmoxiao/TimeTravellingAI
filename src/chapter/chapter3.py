import pygame
import sys,time

# 初始化Pygame
pygame.init()

# 屏幕尺寸设置
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("维多利亚时代的伦敦")
font = pygame.font.Font("../../fonts/SimHei.ttf", 36)
# 加载大街图片、商店内部图片等资源
street_image = pygame.transform.scale(pygame.image.load("../../pic/chapter3street.png"),(screen_width,screen_height))
store_image = pygame.transform.scale(pygame.image.load("../../pic/chapter3store.png"),(screen_width,screen_height))
rainy_street_image = pygame.transform.scale(pygame.image.load("../../pic/chapter3rainy_street.png"),(screen_width,screen_height))
win_image = pygame.transform.scale(pygame.image.load("../../pic/chapter3win.png"),(screen_width,screen_height))
bookpage=pygame.transform.scale(pygame.image.load("../../pic/chapter3bookpage.png"),(screen_width,screen_height))
idea=pygame.transform.scale(pygame.image.load("../../pic/idea.png"),(300,300))
# 一些用于游戏状态控制的变量
current_image = street_image
show_text = False
game_won = False
hidden1=False
hidden2=False
hint=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            print(x,y)
            if 1730<=x<=1821 and 96<=y<=246:
                hint=(not hint)
            if current_image == street_image:
                # 点击人物显示文字的逻辑（
                if 817<=x<=878 and 604<=y<=956:
                    show_text = True
                # 点击商店的逻辑
                elif 0<=x<=778 and 341<=y<=990:
                    current_image = store_image
                    show_text = False
            elif current_image == store_image:
                # 点击遥控器的逻辑
                if 876<=x<=881 and 321<=y<=329:
                    current_image = rainy_street_image
                elif 63<=x<=249 and 1000<=y<=1038:
                    current_image=street_image
            elif current_image == rainy_street_image:
                # 点击隐藏物品的计数逻辑（这里两个隐藏物品，实际需精确判断位置）
                #hidden_items_clicked = 0
                if 1397<=x<=1439 and 1016<=y<=1048:
                    #hidden_items_clicked += 1
                    hidden1=True
                    screen.blit(font.render("你找到了隐藏物品发条", True, (255, 255, 255)), (50, 50))
                    pygame.display.flip()
                    print(hidden1,hidden2)
                if 1740<=x<=1751 and 961<=y<=972:
                    hidden2=True
                    screen.blit(font.render("你找到了隐藏物品玻璃球", True, (255, 255, 255)), (50, 50))
                    pygame.display.flip()
                    print(hidden1,hidden2)
                if 692<=x<=755 and 700<=y<=728:
                    current_image=bookpage
                    screen.blit(current_image, (0, 0))
                    font = pygame.font.Font("../../fonts/SimHei.ttf", 36)
                    tmp=50
                    text = "我可以给你提供一些线索，但是这是有代价的\n你需要找到一个发条和一个灰色珠子\n为了赔偿你打扰我的精神损失费：\n你需要等待一坤分（两分半）才能返回大街\n还有，请公平的游戏".split("\n")
                    for line in text:
                        screen.blit(font.render(line, True, (255, 255, 255)), (50, tmp))
                        tmp+=50
                    #font.render("我可以给你提供一些线索，但是这是有代价的\n你需要找到一个发条和一个灰色珠子\n为了赔偿你打扰我的精神损失费：\n你需要等待一坤分（两分半）才能返回大街", True, (255, 255, 255))
                    #screen.blit(text, (50, 50))

                    pygame.display.flip()
                    for i in range(150):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.display.flip()
                                
                        pygame.display.flip()
                        time.sleep(1)
                    current_image=rainy_street_image
                if hidden1 and hidden2:
                    game_won = True

    screen.blit(current_image, (0, 0))
    screen.blit(idea, (screen_width-300, 10))
    if hint:
        text = font.render("你来到了维多利亚时代的伦敦，你需要找到两个隐藏物品，来激活时间机器，去往未来。小心一语双关！", True, (255, 255, 255))
        screen.blit(text, (50,100))
    if show_text:

        text = font.render("玩具店，合适的工具", True, (255, 255, 255))
        screen.blit(text, (830, 604))
    if game_won:
        screen.blit(win_image, (0, 0))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    pygame.display.flip()