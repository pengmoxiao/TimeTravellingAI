import pygame
import random
import sys,time

# 初始化 Pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
background=pygame.image.load("../pic/chapter2bg.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("中世纪的城堡 - 解锁数字锁")
notice=pygame.image.load("../pic/chapter2notice.jpg")
image = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
notice=pygame.transform.scale(notice,(SCREEN_WIDTH,SCREEN_HEIGHT))
# 颜色设置
winimg = pygame.transform.scale(pygame.image.load("../pic/chapter2win.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
# 字体设置
font = pygame.font.Font("../fonts/SimHei.ttf", 36)
big_font = pygame.font.Font("../fonts/SimHei.ttf", 48)

historical_events = [
    ("城堡建造", random.randint(1000, 1100)),
    ("第一次大战", random.randint(1100, 1200)),
    ("第二次大战", random.randint(1200, 1300)),
    ("魔法物品封印", random.randint(1300, 1400)),
    ("城堡重建", random.randint(1400, 1500)),
    ("最后的守卫战", random.randint(1500, 1600)),
]

# 密码
correct_password = [int(num) for num in str(historical_events[0][1]+historical_events[-1][1])]
#贪心的密码
cupidity_pwd = [int(num) for num in str(historical_events[3][1])]
# 游戏状态
user_input = []
game_over = False
input_pos = 0
attemps =0 
# 控制是否展示历史事件
show_events = False

# 游戏循环
def game_loop():
    global user_input, input_pos, game_over, show_events,attemps
    while True:
        #screen.fill(WHITE)
        screen.blit(image,(0,0))
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                # 点击查看历史事件
                x, y = event.pos
                #print(x,y)
                if (438 <= x <= 564 and 147 <= y <= 352) or (1353<=x<=1469 and 131<=y<=346):  # 点击"查看历史事件"区域
                    show_events = True
                    #pass  # 显示历史事件

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # 检查密码是否正确
                    #print(user_input,correct_password)
                    """
                    if user_input == [1,1,4,5,1,4]:
                        game_over = True  # 作弊
                        """
                    if user_input == correct_password:
                        #print(user_input,correct_password)
                        game_over = True  # 设置游戏结束
                    else:
                        
                        attemps+=1
                        #error = font.render(f"密码错误,你还有{3-attemps}次机会", True, RED)
                        #screen.blit(error, (50, 100))
                        if user_input==cupidity_pwd:
                            error = big_font.render(f"没想到你是这么贪心！欲速则不达！", True, RED)
                            screen.blit(error, (SCREEN_WIDTH // 4+100, SCREEN_HEIGHT // 2))
                            pygame.display.update()

                            time.sleep(3)
                            pygame.quit()
                            sys.exit()
                        if attemps==5:
                            error = big_font.render(f"密码错误次数过多，游戏结束", True, RED)
                            screen.blit(error, (SCREEN_WIDTH // 4+200, SCREEN_HEIGHT // 2))
                            pygame.display.update()

                            time.sleep(3)
                            pygame.quit()
                            sys.exit()
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

        # 显示历史事件或密码输入界面
        if show_events:
            show_historical_events()
        else:
            draw_input()

        # 显示游戏结束的界面
        if game_over:
            draw_game_over()
            pygame.display.update()
            time.sleep(3)    # 等待3秒后退出游戏
            pygame.quit()
            sys.exit()

        pygame.display.update()

def draw_input():
    """绘制当前密码输入"""
    text = "       输入密码: "
    for i in range(input_pos):
        text += str(user_input[i])
    input_text = big_font.render(text, True, WHITE)
    screen.blit(input_text, (70, 70))

def draw_game_over():
    """绘制游戏结束的界面"""
    text = "密码正确,恭喜获得魔法物品"
    screen.blit(winimg,(0,0))

    game_over_text = big_font.render(text, True, GOLD)
    screen.blit(game_over_text, (SCREEN_WIDTH // 4+200, SCREEN_HEIGHT // 2))
    

def show_historical_events():
    """显示城堡的历史事件"""
    event_texts = ["The History of Plusburg","加法堡的历史：","这座城堡是为了纪念加法王一世的登基而建成的。",
    "在最后的守卫战中，加法王国王寡不敌众，",
    "只好封禁城堡，弃城而逃",
    "勇敢的冒险家，唯有你能细心的",
    "破解出加法王的密码，",
    "获得里面的魔法物品"]
    for event, year in historical_events:
        event_texts.append(f"{event} - {year}")
    #screen.fill(WHITE)
    screen.blit(notice,(0,0))
    # 显示历史事件
    y_offset = 70
    for text in event_texts:
        event_render = font.render(text, True, BLACK)
        screen.blit(event_render, (70, y_offset))
        y_offset += 45

    # 显示返回按钮
    back_button_text = font.render("点击此处返回", True, BLUE)
    screen.blit(back_button_text, (50, SCREEN_HEIGHT - 100))

    # 检测返回按钮点击区域
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:  # 左键点击
        if 50 <= mouse_x <= 250 and SCREEN_HEIGHT - 100 <= mouse_y <= SCREEN_HEIGHT:
            global show_events
            show_events = False  # 返回到密码输入界面

# 启动游戏循环
game_loop()