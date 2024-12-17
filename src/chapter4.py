import pygame
import sys

# 初始化Pygame
pygame.init()

# 屏幕设置
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("未来城市 电路谜题")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 电路板组件类
class CircuitComponent(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, active=False):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.active = active

    def activate(self):
        self.active = True
        self.image.fill(GREEN)

    def deactivate(self):
        self.active = False
        self.image.fill(RED)

# 电路板类，管理所有的组件
class CircuitBoard:
    def __init__(self):
        self.components = pygame.sprite.Group()
        self.create_components()

    def create_components(self):
        # 创建开关按钮，位置和尺寸可以根据需要调整
        self.switch1 = CircuitComponent(100, 100, 50, 50, RED)
        self.switch2 = CircuitComponent(200, 100, 50, 50, RED)
        self.switch3 = CircuitComponent(300, 100, 50, 50, RED)
        self.board1 = CircuitComponent(500, 100, 50, 50, BLUE)
        self.board2 = CircuitComponent(600, 100, 50, 50, BLUE)
        
        self.components.add(self.switch1, self.switch2, self.switch3, self.board1, self.board2)

    def check_circuit(self):
        # 如果所有开关都被激活，电路就连接成功
        if self.switch1.active and self.switch2.active and self.switch3.active:
            self.board1.activate()
            self.board2.activate()
            return True
        return False

    def draw(self, screen):
        self.components.draw(screen)

# 游戏主循环
def main():
    clock = pygame.time.Clock()
    running = True
    circuit_board = CircuitBoard()

    while running:
        screen.fill(WHITE)

        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 点击事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # 检测是否点击了开关
                for component in circuit_board.components:
                    if component.rect.collidepoint(mouse_x, mouse_y):
                        if component == circuit_board.switch1:
                            component.activate() if not component.active else component.deactivate()
                        elif component == circuit_board.switch2:
                            component.activate() if not component.active else component.deactivate()
                        elif component == circuit_board.switch3:
                            component.activate() if not component.active else component.deactivate()

        # 检查电路是否连接成功
        if circuit_board.check_circuit():
            font = font = pygame.font.Font("../fonts/SimHei.ttf", 36)
            text = font.render("电路已激活！", True, (0, 128, 0))
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2))

        # 绘制所有组件
        circuit_board.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
