import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置屏幕尺寸和颜色
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("维多利亚时代的伦敦")

# 加载字体
font = pygame.font.Font("fonts/SimHei.ttf", 36)

# 摊位类
class Stall:
    def __init__(self, name, clue):
        self.name = name
        self.clue = clue
        self.rect = pygame.Rect(random.randint(50, 700), random.randint(50, 500), 150, 100)

    def draw(self):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        text = font.render(self.name, True, FONT_COLOR)
        screen.blit(text, (self.rect.x + 10, self.rect.y + 10))

# 创建摊位
stalls = [
    Stall("古董摊位", "你需要找到一个发条装置。"),
    Stall("书摊", "在书页中可能藏有线索。"),
    Stall("玩具摊位", "小玩具可能是关键。"),
]

# 游戏主循环
running = True
found_clues = []

while running:
    screen.fill(BACKGROUND_COLOR)

    # 绘制摊位
    for stall in stalls:
        stall.draw()

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for stall in stalls:
                if stall.rect.collidepoint(mouse_pos):
                    found_clues.append(stall.clue)
                    stalls.remove(stall)  # 移除已访问的摊位
                    print(f"你发现了线索: {stall.clue}")

    # 显示已找到的线索
    clue_text = font.render("已找到的线索:", True, FONT_COLOR)
    screen.blit(clue_text, (20, 20))
    for i, clue in enumerate(found_clues):
        text = font.render(clue, True, FONT_COLOR)
        screen.blit(text, (20, 60 + i * 30))

    pygame.display.flip()

# 退出 Pygame
pygame.quit()
