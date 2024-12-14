import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FONT_SIZE = 24
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (200, 200, 200)
BUTTON_COLOR = (50, 50, 150)
HOVER_COLOR = (100, 100, 200)

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ancient Pyramid Adventure")

# Font setup
font = pygame.font.Font("fonts/Arial Unicode MS.ttf", FONT_SIZE)

# Sample hieroglyphic puzzle data
puzzle_data = [
    {"symbol": "☯", "options": ["Sun", "Pharaoh", "Peace"], "correct": "Peace"},
    {"symbol": "☀", "options": ["Moon", "Sun", "Star"], "correct": "Sun"},
    {"symbol": "✡", "options": ["Star", "Life", "Sun"], "correct": "Star"},
]

current_question = 0
selected_option = None

def render_text(text, x, y, color=TEXT_COLOR):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def render_question():
    global puzzle_data, current_question,running
    if running:
        screen.fill(BG_COLOR)
        question = puzzle_data[current_question]
        render_text(f"Symbol: {question['symbol']}", 50, 50)

        for i, option in enumerate(question['options']):
            option_color = BUTTON_COLOR
            if selected_option == i:
                option_color = HOVER_COLOR
            pygame.draw.rect(screen, option_color, (50, 150 + i * 50, 200, 40))
            render_text(option, 60, 160 + i * 50)

def check_answer():
    global current_question, selected_option
    if selected_option is not None:
        question = puzzle_data[current_question]
        if question['options'][selected_option] == question['correct']:
            return True
    return False


# Main game loop

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(len(puzzle_data[current_question]['options'])):
                if 50 <= x <= 250 and 150 + i * 50 <= y <= 190 + i * 50:
                    selected_option = i
                    if check_answer():
                        current_question += 1
                        selected_option = None
                        if current_question >= len(puzzle_data):
                            print("You solved all puzzles!")
                            running = False

    render_question()
    pygame.display.flip()
    clock.tick(30)
import chapter2
pygame.quit()
sys.exit()

