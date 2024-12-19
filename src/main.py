import pygame, sys,time

# 初始化
pygame.init()
screen_width = 1920 
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height),pygame.FULLSCREEN)
pygame.display.set_caption("时间旅行解谜游戏")
icon = pygame.image.load('../icon.png')
pygame.display.set_icon(icon)

# 定义字体
font = pygame.font.Font("../fonts/SimHei.ttf", 25)
big_font = pygame.font.Font("../fonts/SimHei.ttf", 50)

# 渲染游戏标题文本
title_text = font.render("时间旅行解谜", True, (255, 255, 255))
title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))

# 渲染开始游戏提示文本
start_text = font.render("走到迷宫出口按空格键开始游戏", True, (255, 255, 255))
start_rect = start_text.get_rect(center=(screen_width // 2, screen_height // 3))

# 迷宫相关设置
maze_width = 150
maze_height = 150
maze_x = (screen_width - maze_width) // 2
maze_y = (screen_height - maze_height) // 2
wall_color = (100, 100, 100)
player_size = 20
player_color = (255, 0, 0)
player_x = maze_x + 20
player_y = maze_y + 20

# 修正后的简单迷宫布局，0表示通道，1表示墙壁
maze_layout = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# 设置出口位置，确保它在通道上
exit_x = maze_x + 80
exit_y = maze_y + 100
exit_size = 20
exit_color = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# 时间控制
move_interval = 200  # 单位为毫秒（每0.5秒移动一次）
last_move_time = 0

# 游戏主循环
clock = pygame.time.Clock()
text="Dehou Studio Presents:\nTime Travelling Riddle Game".split("\n")
for i in range(255):
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    color=(i,i,i)
    screen.blit(big_font.render(text[0], True, color), big_font.render(text[0], True, WHITE).get_rect(center=(screen_width // 2, screen_height // 3)))
    screen.blit(big_font.render(text[1], True, color), big_font.render(text[1], True, WHITE).get_rect(center=(screen_width // 2, screen_height // 3+100)))
    pygame.display.update()
    time.sleep(0.01)
for i in range(255,0,-1):
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    color=(i,i,i)
    screen.blit(big_font.render(text[0], True, color), big_font.render(text[0], True, WHITE).get_rect(center=(screen_width // 2, screen_height // 3)))
    screen.blit(big_font.render(text[1], True, color), big_font.render(text[1], True, WHITE).get_rect(center=(screen_width // 2, screen_height // 3+100)))
    pygame.display.update()
    time.sleep(0.01)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取当前按键状态
    keys = pygame.key.get_pressed()

    # 获取当前时间
    current_time = pygame.time.get_ticks()

    # 每隔 move_interval 毫秒处理一次移动
    if current_time - last_move_time >= move_interval:
        if keys[pygame.K_UP]:
            new_y = player_y - player_size
            if new_y >= maze_y and maze_layout[(new_y - maze_y) // player_size][(player_x - maze_x) // player_size] == 0:
                player_y = new_y

        if keys[pygame.K_DOWN]:
            new_y = player_y + player_size
            if new_y <= maze_y + maze_height - player_size and maze_layout[(new_y - maze_y) // player_size][(player_x - maze_x) // player_size] == 0:
                player_y = new_y

        if keys[pygame.K_LEFT]:
            new_x = player_x - player_size
            if new_x >= maze_x and maze_layout[(player_y - maze_y) // player_size][(new_x - maze_x) // player_size] == 0:
                player_x = new_x

        if keys[pygame.K_RIGHT]:
            new_x = player_x + player_size
            if new_x <= maze_x + maze_width - player_size and maze_layout[(player_y - maze_y) // player_size][(new_x - maze_x) // player_size] == 0:
                player_x = new_x

        # 更新最后移动的时间戳
        last_move_time = current_time

    # 判断是否按下空格键以及是否到达出口
    if keys[pygame.K_SPACE]:
        if (
            player_x + player_size >= exit_x
            and player_x <= exit_x + exit_size
            and player_y + player_size >= exit_y
            and player_y <= exit_y + exit_size
        ):
            print("开始游戏啦，后续可添加具体逻辑")
            import chapter1
            #chapter2.game_loop()
            #exit()

    screen.fill((0, 0, 0))

    # 绘制迷宫墙壁
    for row in range(len(maze_layout)):
        for col in range(len(maze_layout[row])):
            if maze_layout[row][col] == 1:
                pygame.draw.rect(screen, wall_color, (maze_x + col * player_size, maze_y + row * player_size, player_size, player_size))

    # 绘制玩家方块
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # 绘制出口方块
    pygame.draw.rect(screen, exit_color, (exit_x, exit_y, exit_size, exit_size))

    # 在屏幕上绘制游戏标题
    screen.blit(title_text, title_rect)

    # 在屏幕上绘制开始游戏提示
    screen.blit(start_text, start_rect)

    # 更新显示
    pygame.display.flip()
    clock.tick(60)
