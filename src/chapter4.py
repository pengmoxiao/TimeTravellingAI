from os import error
import pygame
import sys
import random
from time import sleep
pygame.init()

# 设置窗口大小
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("未来城市电路谜题")
one=bookpage=pygame.transform.scale(pygame.image.load("../pic/chapter4_1.png"),(WINDOW_WIDTH,WINDOW_HEIGHT))
boom=bookpage=pygame.transform.scale(pygame.image.load("../pic/chapter4_boom.jpg"),(WINDOW_WIDTH,WINDOW_HEIGHT))
font = pygame.font.Font("../fonts/SimHei.ttf", 36)
# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
font = pygame.font.Font("../fonts/SimHei.ttf", 36)
# 当前关卡
current_level = 1
# 用于存储电路相关的对象等（这里简单示例，可根据实际细化）
circuits = []
# 记录各关卡完成状态
levels_completed = [False] * 4

# 用于模拟电路开关状态（示例简单用列表表示，可根据实际复杂程度改对象等）
switch_states = [False] * 3 # 假设有5个开关，可调整数量

# 用于第二题错误导线相关（示例简单用索引表示要移除的导线，可根据实际复杂程度改对象等）
wrong_wire_index = None
# 用于第三题电流表读数相关，这里随机生成一个示例正确读数（范围可根据实际调整）
correct_ammeter_reading = round(random.uniform(0, 10), 2)
# 用于第四题电路图片对应的正确数字
correct_number_for_circuit_image = None

# 输入框相关变量
input_box = pygame.Rect(300, 250, 200, 40)
input_text = ""
active = False
input_pos = 0
user_input = []
def draw_input():
    global user_input,input_pos,input_text
    """绘制当前密码输入"""
    text = "       输入密码: "
    for i in range(input_pos):
        text += str(user_input[i])
    input_text = font.render(text, True, WHITE)
    screen.blit(input_text, (70, 70))
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
    if current_level==4:
        print("Yes")
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        input_surface = font.render(input_text, True, BLACK)
        screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))
    
    pygame.display.flip()

def handle_level1():
    global current_level
    # 假设正确的开关状态组合（这里简单示例，可按实际改复杂逻辑）
    error_combination=[True,True,True]
    if current_level==1:
        correct_combination = [False,True,False]
    if current_level==2:
        correct_combination = [True,False,True]
    #print(switch_states)
    if switch_states==error_combination:
        screen.blit(boom, (0, 0))
        pygame.display.flip()
        tmp=50
        text = "电池短路爆炸了\n你需要等待一坤分（两分半）才能继续游戏\n还有，请公平的游戏".split("\n")
        for line in text:
            screen.blit(font.render(line, True, (255, 255, 255)), (50, tmp))
            tmp+=50
        for i in range(150):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.flip()
                    
            pygame.display.flip()
            sleep(1)
    if switch_states == correct_combination:
        #levels_completed[0] = True
        print(current_level,type(current_level))
        if current_level==1:
            current_level =2
        elif current_level==2:
            current_level =3

def handle_level2():
    global current_level
    if wrong_wire_index is None:
        # 这里假设通过某种交互已经移除了错误导线，简单示例直接设置完成
        #levels_completed[1] = True
        current_level = 3

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
    global user_input,input_pos,input_text
    correct_number_for_circuit_image=[1]
    for event in pygame.event.get():
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
                        input_pos += 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 判断鼠标点击是否在开关区域来切换开关状态并更新显示颜色
            mouse_x, mouse_y = pygame.mouse.get_pos()
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
    print(current_level)
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
        draw_circuit()
        handle_level4()

    pygame.display.update()