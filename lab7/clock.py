import pygame                  # Importing pygame library / Pygame кітапханасын қосу
import datetime                # Importing datetime to get current time / Қазіргі уақытты алу үшін datetime қосу

pygame.init()                  # Initializing pygame / Pygame-ді инициализациялау
W, H = 600, 400                # Width and height of the screen / Экран ені мен биіктігі
sc = pygame.display.set_mode((W, H))  # Creating the screen window / Терезе жасау
pygame.display.set_caption("Mickey Clock")  # Window title / Терезе атауы


# Function to display current time (MM:SS) / Қазіргі уақытты (Минут:Секунд) көрсету функциясы
def system_time(now):
    global time_font

    min = now.strftime('%M')  # Get current minute / Ағымдағы минутты алу
    sec = now.strftime('%S')  # Get current second / Ағымдағы секундты алу

   

# Loading clock and hand images / Сағат пен тілдердің суреттерін жүктеу
clock_sc = pygame.image.load('/Users/kassymgulnaz/Desktop/pp2/labs/lab7/images/clock.png').convert_alpha()
leftarm_sc = pygame.image.load('/Users/kassymgulnaz/Desktop/pp2/labs/lab7/images/sec_hand.png').convert_alpha()
rightarm_sc = pygame.image.load('/Users/kassymgulnaz/Desktop/pp2/labs/lab7/images/min_hand.png').convert_alpha()

# Resizing images / Суреттер өлшемін өзгерту
clock_sc = pygame.transform.scale(clock_sc, (W, H))  # Clock background to fit screen / Сағат фонын экранға лайықтау
leftarm_sc = pygame.transform.scale(leftarm_sc, (leftarm_sc.get_width()//2.0, leftarm_sc.get_height()//2.0))  # Second hand / Секунд тілі
rightarm_sc = pygame.transform.scale(rightarm_sc, (rightarm_sc.get_width()//2.0, rightarm_sc.get_height()//1.2))  # Minute hand / Минут тілі

angle = 0  # Initial angle for rotation / Айналу бұрышы

clock = pygame.time.Clock()  # Create clock object to manage FPS / FPS басқару үшін сағат объектісі

# Get the center position of clock for rotation / Сағат ортасын көрсету үшін
leftarm_rect = leftarm_sc.get_rect(center=(W//2, H//2))
rightarm_rect = rightarm_sc.get_rect(center=(W//2, H//2))

# Draw initial hands (not rotated yet) / Бастапқы тілдерді экранға салу (айналмаған)
sc.blit(leftarm_sc, leftarm_rect)
sc.blit(rightarm_sc, rightarm_rect)

# Main loop / Негізгі цикл
while 1:
    for event in pygame.event.get():         # Event handling / Оқиғаларды тексеру
        if event.type == pygame.QUIT:        # If window close is requested / Егер терезені жабу сұралса
            exit()                           # Exit the program / Бағдарламадан шығу

    now = datetime.datetime.now()            # Get current system time / Жүйелік уақытты алу
    sc.fill((255, 255, 255))                 # Clear screen with white / Экранды ақ түспен бояу
    sc.blit(clock_sc, (0, 0))                # Draw clock background / Сағат фонын салу

    # Calculate rotation angles / Айналу бұрыштарын есептеу
    angle = -(now.second + 1) * 6            # Second hand: 6 degrees per second / Секунд тілі: әр секундқа 6 градус
    angle2 = -(now.minute) * 6               # Minute hand: 6 degrees per minute / Минут тілі: әр минутқа 6 градус

    # Rotate second hand image / Секунд тіліне бұру анимациясы
    leftarm_sc_rotated = pygame.transform.rotate(leftarm_sc, angle)
    leftarm_rect_rotated = leftarm_sc_rotated.get_rect(center=leftarm_rect.center)

    # Rotate minute hand image / Минут тіліне бұру анимациясы
    rightarm_sc_rotated = pygame.transform.rotate(rightarm_sc, angle2 - 54)  # -54 to adjust image alignment / сурет бағытын түзету
    rightarm_rect_rotated = rightarm_sc_rotated.get_rect(center = rightarm_rect.center)

    # Draw rotated hands on screen / Айналған тілдерді экранға салу
    sc.blit(leftarm_sc_rotated, leftarm_rect_rotated)
    sc.blit(rightarm_sc_rotated, rightarm_rect_rotated)

    system_time(now)                         # Draw digital time / Цифрлы уақытты жазу
    
    pygame.display.update()                  # Update the display / Экранды жаңарту
    clock.tick(1)                            # Wait 1 second (1 frame per second) / 1 секунд сайын жаңарту