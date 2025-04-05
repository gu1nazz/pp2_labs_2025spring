import pygame
import random

pygame.init()

# Экран өлшемдері
WIDTH, HEIGHT = 500, 700 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Суреттер
car_img = pygame.image.load("/Users/kassymgulnaz/Desktop/pp2/labs/lab9/carr.png")
coin_img = pygame.image.load("/Users/kassymgulnaz/Desktop/pp2/labs/lab9/coin.png")
road_img = pygame.image.load("/Users/kassymgulnaz/Desktop/pp2/labs/lab9/road.jpg")
enemy_img = pygame.image.load("/Users/kassymgulnaz/Desktop/pp2/labs/lab9/Enemyy.png")

# Өлшемдер
car_width, car_height = 70, 140
coin_width, coin_height = 40, 40
enemy_width, enemy_height = 70, 140

# Масштабтау
car_img = pygame.transform.scale(car_img, (car_width, car_height))
coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))
enemy_img = pygame.transform.scale(enemy_img, (enemy_width, enemy_height))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Шрифт
font = pygame.font.Font(None, 36)

# Түстер
WHITE = (255, 255, 255)

# --- RESET функция ---
def reset():
    global car_x, car_y, coin_x, coin_y, coin_value, enemy_x, enemy_y, enemy_speed, score
    car_x = WIDTH // 2 - car_width // 2
    car_y = HEIGHT - car_height - 20
    coin_x = random.randint(100, WIDTH - 100)
    coin_y = -50
    coin_value = random.choice([1, 2, 3])
    enemy_x = random.randint(100, WIDTH - 100)
    enemy_y = -150
    enemy_speed = 7
    score = 0

# --- Алғашқы инициализация ---
reset()
car_speed = 5
coin_speed = 7

clock = pygame.time.Clock()
running = True

while running:
    screen.blit(road_img, (0, 0))
    screen.blit(car_img, (car_x, car_y))
    screen.blit(coin_img, (coin_x, coin_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))

    # Оқиғалар
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Көлік қозғалуы
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 10:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width - 10:
        car_x += car_speed

    # Монета қозғалуы
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(100, WIDTH - 100)

    # Дұшпан қозғалуы
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -150
        enemy_x = random.randint(100, WIDTH - 100)

    # Монетаны жинау
    if (car_x < coin_x + coin_width and car_x + car_width > coin_x) and \
       (car_y < coin_y + coin_height and car_y + car_height > coin_y):
        score += coin_value
        coin_y = -50
        coin_x = random.randint(100, WIDTH - 100)
        coin_value = random.choice([1, 2, 3])
        if score % 5 == 0:
            enemy_speed += 1

    # 🟥 Дұшпанмен соқтығысса — ойын қайта басталады
    if (car_x < enemy_x + enemy_width and car_x + car_width > enemy_x) and \
       (car_y < enemy_y + enemy_height and car_y + car_height > enemy_y):
        pygame.time.delay(500)
        reset()

    # Ұпай шығару
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()