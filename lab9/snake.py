import pygame
import random
import time

pygame.init()

# Экран параметрлері
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Түстер
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Бастапқы параметрлер
snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)
score = 0
level = 1
speed = 10

# Тамақ жасау функциясы (жоғалып кету уақытымен)
def generate_food():
    pos = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
    value = random.choice([1, 2, 3])  # Ұпай (салмақ)
    timer = time.time()  # Қашан пайда болғанын сақтаймыз
    return {"pos": pos, "value": value, "time": timer}

food = generate_food()

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # Оқиғаларды өңдеу
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)

    # Жаңа бас координатасы
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # Қабырғаға немесе өзіне тигенін тексеру
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        running = False
        break

    snake.insert(0, new_head)

    # ⏱️ Тамақ жоғалып кете ме?
    if time.time() - food["time"] > 5:  # 5 секундтан кейін жоғалады
        food = generate_food()

    # 🍎 Тамақ жегенде
    if new_head == food["pos"]:
        score += food["value"]
        if score % 4 == 0:
            level += 1
            speed += 2
        food = generate_food()
    else:
        snake.pop()

    # Тамақты экранға шығару (размері value-ге байланысты сәл үлкенірек)
    size = CELL_SIZE + (food["value"] - 1) * 5  # value=1 → 20, value=3 → 30
    food_rect = pygame.Rect(food["pos"][0], food["pos"][1], size, size)
    pygame.draw.rect(screen, RED, food_rect)

    # Жыланды салу
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))

    # Ұпай мен деңгей шығару
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()