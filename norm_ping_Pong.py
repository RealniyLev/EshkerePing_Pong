import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Classic")

# Цвета
WHITE = (255, 255, 255)


# Шрифт
font = pygame.font.SysFont("Arial", 50)


score_player1 = 0
score_player2 = 0

# Загрузка изображений
try:
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    
    rocket_img = pygame.image.load("rocketka.png")
    rocket_img = pygame.transform.scale(rocket_img, (20, 100))
    
    ball_img = pygame.image.load("ball.jpg")
    ball_img = pygame.transform.scale(ball_img, (30, 30))
except:
    print("Ошибка: Проверь, что файлы картинок лежат в папке с кодом!(ball.jpg, rocketka.png, background.jpg")
    
    pygame.quit()
    sys.exit()

player1_rect = rocket_img.get_rect(midleft=(20, HEIGHT // 2))
player2_rect = rocket_img.get_rect(midright=(WIDTH - 20, HEIGHT // 2))
ball_rect = ball_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

paddle_speed = 7
ball_speed_x = 5
ball_speed_y = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_rect.top > 0:
        player1_rect.y -= paddle_speed
    if keys[pygame.K_s] and player1_rect.bottom < HEIGHT:
        player1_rect.y += paddle_speed
    
    if keys[pygame.K_UP] and player2_rect.top > 0:
        player2_rect.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_rect.bottom < HEIGHT:
        player2_rect.y += paddle_speed

    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect):
        ball_speed_x *= -1

    # --- ИЗМЕНЕНО: Обработка гола ---
    if ball_rect.left <= 0:
        score_player2 += 1  # Очко правому игроку
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    if ball_rect.right >= WIDTH:
        score_player1 += 1  # Очко левому игроку
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    # Отрисовка
    screen.blit(background, (0, 0))
    
    # --- НОВОЕ: Отрисовка счета на экране ---
    # Создаем поверхности с текстом (True — сглаживание)
    score_text = font.render(f"{score_player1} : {score_player2}", True, WHITE)
    # Рисуем счет по центру сверху
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    screen.blit(rocket_img, player1_rect)
    screen.blit(rocket_img, player2_rect)
    screen.blit(ball_img, ball_rect)

    pygame.display.flip()
    clock.tick(60)