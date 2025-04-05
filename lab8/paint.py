import pygame

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint на Pygame")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Начальные переменные
running = True
drawing = False
mode = "pen"  # pen, rect, circle, eraser
color = BLACK
start_pos = (0, 0)

# Основной цикл
screen.fill(WHITE)  # Заливаем фон белым
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Выбор инструмента
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

        # Начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Рисование
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pen":
                pygame.draw.line(screen, color, start_pos, event.pos, 3)
                start_pos = event.pos
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, 10)

        # Завершение рисования фигур
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if mode == "rect":
                rect_width = abs(end_pos[0] - start_pos[0])
                rect_height = abs(end_pos[1] - start_pos[1])
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], rect_width, rect_height), 2)
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

    pygame.display.flip()

pygame.quit()

'''
mouse(lkm)-draw
/var/folders/y4/29t0t48921d7bpskn83skcbr0000gn/T/com.apple.useractivityd/shared-pasteboard/items/C7DBD01D-0EAE-4826-A66E-1FE86FB0EF8C/db4b68f3a3c650eee8d16d61ed24d68b11cf4692.rtfd
'''