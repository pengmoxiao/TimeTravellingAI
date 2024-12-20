from os import error
import pygame
import sys
import random,time
from time import sleep
pygame.init()

# 设置窗口大小
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("未来城市电路谜题")
one=pygame.transform.scale(pygame.image.load("../pic/chapter4_1.png"),(WINDOW_WIDTH,WINDOW_HEIGHT))
boom=pygame.transform.scale(pygame.image.load("../pic/chapter4_boom.jpg"),(WINDOW_WIDTH,WINDOW_HEIGHT))
four=pygame.transform.scale(pygame.image.load("../pic/chapter4_4.png"),(WINDOW_WIDTH,WINDOW_HEIGHT))
end=pygame.transform.scale(pygame.image.load("../pic/the_end.png"),(WINDOW_WIDTH,WINDOW_HEIGHT))
idea=pygame.transform.scale(pygame.image.load("../pic/idea.png"),(300,300))
logo=pygame.transform.scale(pygame.image.load("../pic/Logo.png"),(500,500))
font = pygame.font.Font("../fonts/SimHei.ttf", 36)
# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

Ammeter1 = round(random.uniform(0.7, 1.5), 1)
Ammeter2 = round(random.uniform(0.7, 1.5), 1)
Ammeter = round(random.uniform(1.5, Ammeter1+Ammeter2), 1)
i = Ammeter-Ammeter2
ii = round(Ammeter1 -i,1)
iii = Ammeter-Ammeter1
# 当前关卡
current_level = 1
# 用于存储电路相关的对象等（这里简单示例，可根据实际细化）
circuits = []
# 记录各关卡完成状态
levels_completed = [False] * 4

# 用于模拟电路开关状态（示例简单用列表表示，可根据实际复杂程度改对象等）
switch_states = [False] * 3 # 假设有3个开关，可调整数量

hint=False
# 用于第三题电流表读数相关，这里随机生成一个示例正确读数（范围可根据实际调整）
#correct_ammeter_reading = round(random.uniform(0, 10), 2)
# 用于第四题电路图片对应的正确数字
correct_number_for_circuit_image = [num for num in str(ii)]
print(correct_number_for_circuit_image)
# 输入框相关变量
input_box = pygame.Rect(300, 250, 200, 40)
input_textL2 = ""
active = False
input_pos = 0
user_input = []
def show_thanks(text):
    for i in range(255):
        tmp=WINDOW_HEIGHT//2-len(text)*25
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        color=(i,i,i)
        for line in text:
            screen.blit(font.render(line, True, color), font.render(line, True, WHITE).get_rect(center=(WINDOW_WIDTH // 2, tmp)))
            tmp+=50
        #screen.blit(font.render(text[1], True, color), font.render(text[1], True, WHITE).get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3+100)))
        pygame.display.update()
        time.sleep(0.01)
    
    for i in range(255,0,-1):
        tmp=WINDOW_HEIGHT//2-len(text)*25
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        color=(i,i,i)
        for line in text:
            screen.blit(font.render(line, True, color), font.render(line, True, WHITE).get_rect(center=(WINDOW_WIDTH // 2, tmp)))
            tmp+=50
        #screen.blit(font.render(text[1], True, color), font.render(text[1], True, WHITE).get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3+100)))
        pygame.display.update()
        time.sleep(0.01)
def draw_input():
    screen.blit(four, (0, 0))
    global user_input,input_pos,input_textL2
    problem=f"电流表A1的示数为：{ str(Ammeter1) }\n电流表A2的示数为：{ str(Ammeter2) }\n电流表A的示数为：{ str(Ammeter) }".split("\n")
    #screen.fill(WHITE)
    tmp=50
    for line in problem:
        screen.blit(font.render(line, True, BLACK), (70, tmp))
        tmp+=50
    """绘制当前密码输入"""
    L1text = "输入L2电流: "
    for i in range(input_pos):
        L1text += str(user_input[i])
    input_textL2 = font.render(L1text, True, BLACK)
    screen.blit(input_textL2, (70, tmp+50))
    
def draw_circuit():
    global current_level,one
    screen.fill(WHITE)
    if current_level==1 :
           # print(current_level)
        screen.blit(one, (0, 0))
        tmp=50
        text = "请打开正确的开关，使两个灯泡串联".split("\n")
        for line in text:
            screen.blit(font.render(line, True, BLACK), (50, tmp))
            tmp+=50
    if current_level==2 :
           # print(current_level)
        screen.blit(one, (0, 0))
        tmp=50
        text = "请打开正确的开关，使两个灯泡并联".split("\n")
        for line in text:
            screen.blit(font.render(line, True, BLACK), (50, tmp))
            tmp+=50
        
    
    
    # 绘制开关
    if current_level==1 or current_level==2:
        for i in range(3):
            switch_width = 50
            switch_height = 20
            if switch_states[i]:
                color=GREEN
            else:
                color=RED
            if i==0:
                pygame.draw.rect(screen, color, (531, 468, 180, 60))
            elif i==1:
                pygame.draw.rect(screen, color, (893, 288, switch_width, 170))
            elif i==2:
                pygame.draw.rect(screen, color, (1228, 160, 180, 45))
    
    '''
    # 绘制电流表示意（简单画个矩形和刻度示意，可完善更像真实电流表外观）
    if current_level==4:
        pygame.draw.rect(screen, BLACK, (400, 150, 100, 50))
        pygame.draw.line(screen, RED, (400, 175), (500, 175), 3)  # 画一条刻度线示例'''

    # 绘制输入框
    #print(current_level)
    '''if current_level==4:
        print("Yes")
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        input_surface = font.render("请输入答案：", True, BLACK)
        screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))'''
    
    #pygame.display.flip()

def handle_level1():
    global current_level,switch_states
    # 假设正确的开关状态组合（这里简单示例，可按实际改复杂逻辑）
    error_combination=[True,True,True]
    if current_level==1:
        correct_combination = [False,True,False]
    if current_level==2:
        correct_combination = [True,False,True]
    #print(switch_states)
    if switch_states==error_combination:
        screen.blit(boom, (0, 0))
        #pygame.display.flip()
        tmp=50
        text = "电池短路爆炸了\n你需要等待一坤分（两分半）才能继续游戏\n还有，请公平的游戏".split("\n")
        for line in text:
            screen.blit(font.render(line, True, (255, 255, 255)), (50, tmp))
            tmp+=50
        for i in range(150):
            screen.fill(WHITE)
            screen.blit(boom, (0, 0))
            tmp=50
            text = "电池短路爆炸了\n你需要等待一坤分（两分半）才能继续游戏\n还有，请公平的游戏".split("\n")
            for line in text:
                screen.blit(font.render(line, True, (255, 255, 255)), (50, tmp))
                tmp+=50
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.flip()
            screen.blit(font.render(f"倒计时：{150-i}秒", True, (255, 255, 255)), (50, 215))      
            pygame.display.update()
            pygame.display.flip()
            sleep(1)
        switch_states=[False,False,False]
    if switch_states == correct_combination:
        #levels_completed[0] = True
        print(current_level,type(current_level))
        if current_level==1:
            current_level =2
        elif current_level==2:
            current_level =3

'''def handle_level2():
    global current_level
    if wrong_wire_index is None:
        # 这里假设通过某种交互已经移除了错误导线，简单示例直接设置完成
        #levels_completed[1] = True
        current_level = 3'''

'''def handle_level3():
    global current_level,input_text
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                try:
                    entered_reading = float(input_text)
                    if entered_reading == correct_ammeter_reading:
                        levels_completed[2] = True
                        current_level = 4
                        input_text = ""
                except ValueError:
                    pass
            else:
                input_text += event.unicode
'''

def handle_level4():
    draw_input()
    global current_level
    global user_input,input_pos,input_textL2
    #correct_number_for_circuit_image=[1]
    '''for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                #entered_number = int(input("请输入电路图片对应的数字: "))  # 简单用控制台输入示例
                if user_input == correct_number_for_circuit_image:
                    print("恭喜你，游戏胜利！")
                    pygame.quit()
                    sys.exit()
                
                else:
                    
                    user_input = []  # 重置输入
                    input_pos = 0
                    pygame.display.update()
            elif event.key == pygame.K_BACKSPACE:
                if input_pos > 0:
                    user_input.pop()
                    input_pos -= 1
            elif pygame.K_0 <= event.key <= pygame.K_9:
                        # 不限数字个数，可以输入更多的数字
                user_input.append(event.key - pygame.K_0)
                input_pos += 1'''


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 判断鼠标点击是否在开关区域来切换开关状态并更新显示颜色
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 1700<=mouse_x<=1848 and 836<=mouse_y<=1024:
                hint=(not hint)
            print(mouse_x,mouse_y)
            '''
            pygame.draw.rect(screen, color, (531, 468, 180, 60))
        elif i==1:
            pygame.draw.rect(screen, color, (893, 288, switch_width, 170))
        elif i==2:
            pygame.draw.rect(screen, color, (1228, 160, 180, 45))
            '''
            for i in range(len(switch_states)):
                if i==0:

                    switch_rect = pygame.Rect(531, 468, 180, 60)
                elif i==1:
                    switch_rect = pygame.Rect(893, 288, 50, 170)
                elif i==2:
                    switch_rect = pygame.Rect(1228, 160, 180, 45)
                if switch_rect.collidepoint(mouse_x, mouse_y):
                    switch_states[i] = not switch_states[i]
        if event.type == pygame.KEYDOWN and current_level==4:
            if event.key == pygame.K_RETURN:
                #entered_number = int(input("请输入电路图片对应的数字: "))  # 简单用控制台输入示例
                if user_input == correct_number_for_circuit_image:
                    #print("恭喜你，游戏胜利！")
                    screen.blit(end, (0, 0))
                    big_font=pygame.font.Font("../fonts/SimHei.ttf", 72)
                    screen.blit(big_font.render("Thanks For Playing", True, (255, 255, 255)), big_font.render("Thanks For Playing", True, (255, 255, 255)).get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT-WINDOW_HEIGHT // 7)))
                    for i in range(5):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.display.flip()
                                
                        pygame.display.flip()
                        time.sleep(1)
                    
                    show_thanks("Time Travelling Riddle Game\n\n鸣谢名单".split("\n"))
                    show_thanks("项目总负责与制作：\n\nDehou Studio:\n803徐博扬\n803彭莫晓".split("\n"))
                    show_thanks("AI工具：\n\n豆包\nChatGPT 4o\nHappyAPI\nDeepL\n通义千问".split("\n"))
                    show_thanks("友情援助：\n\n803朱辰希——绘制电路图\n803周靖航——提供电流表计算代码\n1333机房万老师——提供机房\n1310机房潘老师——提供机房\nGit-2.47.0.2-64-bit.exe\nPython\n给予支持的家长".split("\n"))
                    show_thanks("网站：\n\nai.moxiao.site\nalist.moxiao.site\nwww.52oi.com\nwww.github.com\nwww.bing.com".split("\n"))
                    show_thanks("当然，\n\n还有屏幕前玩游戏的你\n感谢你们的支持！！！".split("\n"))
                    text="(c)2024 Dehou Studio. All Rights Reserved.".split("\n")
                    for i in range(255):
                        tmp=WINDOW_HEIGHT//2-len(text)*25
                        screen.fill(BLACK)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        color=(i,i,i)
                        for line in text:
                            screen.blit(big_font.render(line, True, color), big_font.render(line, True, WHITE).get_rect(center=(WINDOW_WIDTH // 2, tmp-200)))
                            tmp+=50
                        #screen.blit(big_font.render(text[1], True, color), big_font.render(text[1], True, WHITE).get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3+100)))
                        screen.blit(logo,(710,500))
                        pygame.display.update()
                        time.sleep(0.01)
                    
                    for i in range(255,0,-1):
                        tmp=WINDOW_HEIGHT//2-len(text)*25
                        screen.fill(BLACK)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        color=(i,i,i)
                        for line in text:
                            screen.blit(big_font.render(line, True, color), big_font.render(line, True, WHITE).get_rect(center=(WINDOW_WIDTH // 2, tmp-200)))
                            tmp+=50
                        screen.blit(logo,(710,500))
                        #screen.blit(font.render(text[1], True, color), font.render(text[1], True, WHITE).get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3+100)))
                        pygame.display.update()
                        time.sleep(0.01)

                        #screen.blit(font.render(text[1], True, color), font.render(text[1], True, WHITE).get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3+100)))
                        
                    pygame.quit()
                    sys.exit()
                
                else:
                    
                    user_input = []  # 重置输入
                    input_pos = 0
                    
            elif event.key == pygame.K_BACKSPACE:
                if input_pos > 0:
                    user_input.pop()
                    input_pos -= 1
            elif pygame.K_0 <= event.key <= pygame.K_9:
                        # 不限数字个数，可以输入更多的数字
                user_input.append(str(event.key - pygame.K_0))
                input_pos += 1
            elif pygame.K_PERIOD:
                user_input.append(".")
                input_pos += 1
    #print(current_level)
    
    if current_level == 1:
        draw_circuit()
        handle_level1()
    
    elif current_level == 2:
        #print(current_level)
        draw_circuit()
        handle_level1()
    elif current_level == 3:
        #print(current_level)
        '''draw_circuit()
        handle_level3()'''
        current_level=4
    elif current_level == 4:
        #draw_circuit()
        handle_level4()
    screen.blit(idea, (WINDOW_WIDTH-300, WINDOW_HEIGHT-300))
    
    if hint:
        text = font.render("你来到了未来，你需要答出电路谜题才能回到现在", True, BLACK)
        screen.blit(text, (350,WINDOW_HEIGHT-100))
    pygame.display.update()
    pygame.display.flip()