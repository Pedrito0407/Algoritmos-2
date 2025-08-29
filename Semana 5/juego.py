import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Reloj
clock = pygame.time.Clock()
FPS = 60

# Jugador
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 10
player_speed = 7

# Bloques enemigos
enemy_width = 50
enemy_height = 50
enemy_speed = 5
enemies = []

# Puntuación
score = 0
font = pygame.font.SysFont(None, 36)

def draw_window(player_rect, enemies, score):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLUE, player_rect)

    for enemy in enemies:
        pygame.draw.rect(WIN, RED, enemy)

    score_text = font.render(f"Puntuación: {score}", True, BLACK)
    WIN.blit(score_text, (10, 10))
    pygame.display.update()

def main():
    global player_x, enemies, score
    run = True
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    spawn_timer = 0

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += player_speed

        # Crear enemigos
        spawn_timer += 1
        if spawn_timer > 30:
            spawn_timer = 0
            enemy_x = random.randint(0, WIDTH - enemy_width)
            new_enemy = pygame.Rect(enemy_x, -enemy_height, enemy_width, enemy_height)
            enemies.append(new_enemy)

        # Mover enemigos
        for enemy in enemies[:]:
            enemy.y += enemy_speed
            if enemy.colliderect(player_rect):
                print("¡Has sido golpeado! Juego terminado.")
                run = False
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                score += 1

        draw_window(player_rect, enemies, score)

if __name__ == "__main__":
    main()
