import pygame
import math

# Инициализация Pygame
pygame.init()

# Экран параметрлері
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Айнымалылар
running = True
drawing = False
mode = "pen"  # бастапқы режим
color = BLACK
start_pos = (0, 0)

# Фонды ақпен бояймыз
screen.fill(WHITE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Клавиатурадан фигура немесе түс таңдау
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_q:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

        # Тінтуірді басқанда — бастапқы нүктені белгілейміз
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Қозғалыс кезінде — еркін сызу немесе өшіру
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pen":
                pygame.draw.line(screen, color, start_pos, event.pos, 3)
                start_pos = event.pos
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, 10)

        # Тінтуірді жібергенде — фигура салу
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            x1, y1 = start_pos
            x2, y2 = end_pos
            width = x2 - x1
            height = y2 - y1

            if mode == "rect":
                pygame.draw.rect(screen, color, (x1, y1, width, height), 2)

            elif mode == "circle":
                radius = int(math.hypot(x2 - x1, y2 - y1))
                pygame.draw.circle(screen, color, start_pos, radius, 2)

            elif mode == "square":
                side = min(abs(width), abs(height))
                pygame.draw.rect(screen, color, (x1, y1, side * (1 if width > 0 else -1), side * (1 if height > 0 else -1)), 2)

            elif mode == "right_triangle":
                points = [start_pos, (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, color, points, 2)

            elif mode == "equilateral_triangle":
                side = math.hypot(width, height)
                height_tri = (math.sqrt(3) / 2) * side
                direction = 1 if height >= 0 else -1
                points = [
                    start_pos,
                    (x1 + side, y1),
                    (x1 + side / 2, y1 + direction * height_tri)
                ]
                pygame.draw.polygon(screen, color, points, 2)

            elif mode == "rhombus":
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                points = [
                    (center_x, y1),
                    (x2, center_y),
                    (center_x, y2),
                    (x1, center_y)
                ]
                pygame.draw.polygon(screen, color, points, 2)

    pygame.display.flip()

pygame.quit()