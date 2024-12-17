import pygame
import sys
import random

pygame.init()

# 设置窗口大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("未来城市电路谜题")

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
switch_states = [False] * 5  # 假设有5个开关，可调整数量

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

def draw_circuit():
    screen.fill(WHITE)
    # 绘制开关
    switch_width = 50
    switch_height = 20
    for i in range(len(switch_states)):
        if switch_states[i]:
            pygame.draw.rect(screen, GREEN, (100 + i * 80, 100, switch_width, switch_height))
        else:
            pygame.draw.rect(screen, BLACK, (100 + i * 80, 100, switch_width, switch_height))

    # 绘制电流表示意（简单画个矩形和刻度示意，可完善更像真实电流表外观）
    pygame.draw.rect(screen, BLACK, (400, 150, 100, 50))
    pygame.draw.line(screen, RED, (400, 175), (500, 175), 3)  # 画一条刻度线示例

    # 绘制输入框
    pygame.draw.rect(screen, BLACK, input_box, 2)
    input_surface = font.render(input_text, True, BLACK)
    screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    pygame.display.flip()

def handle_level1():
    global current_level
    # 假设正确的开关状态组合（这里简单示例，可按实际改复杂逻辑）
    correct_combination = [True, False, True, False, True]
    print(switch_states)
    if switch_states == correct_combination:
        levels_completed[0] = True
        current_level = 2

def handle_level2():
    global current_level
    if wrong_wire_index is None:
        # 这里假设通过某种交互已经移除了错误导线，简单示例直接设置完成
        levels_completed[1] = True
        current_level = 3

def handle_level3():
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


def handle_level4():
    global current_level
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                entered_number = int(input("请输入电路图片对应的数字: "))  # 简单用控制台输入示例
                if entered_number == correct_number_for_circuit_image:
                    print("恭喜你，游戏胜利！")
                    pygame.quit()
                    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 判断鼠标点击是否在开关区域来切换开关状态并更新显示颜色
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(len(switch_states)):
                switch_rect = pygame.Rect(100 + i * 80, 100, 50, 20)
                if switch_rect.collidepoint(mouse_x, mouse_y):
                    switch_states[i] = not switch_states[i]

    if current_level == 1:
        draw_circuit()
        handle_level1()
    elif current_level == 2:
        #print(current_level)
        draw_circuit()
        handle_level2()
    elif current_level == 3:
        #print(current_level)
        draw_circuit()
        handle_level3()
    elif current_level == 4:
        draw_circuit()
        handle_level4()

    pygame.display.update()