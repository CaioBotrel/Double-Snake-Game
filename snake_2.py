import pygame
from pygame.locals import *
import random

WINDOW_SIZE = (600,600)
PIXEL_SIZE = 10

def collision(pos1, pos2):
    return pos1 == pos2

def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True

def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')
# Create a font object using pygame.font module
myfont = pygame.font.SysFont("Arial", 30)
# Render the "Game Over" text
gameover_text = myfont.render("Game Over", True, (255, 0, 0))


snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((127, 255, 0))
snake_direction = K_LEFT
snake_pos2 = [(300, 250), (310, 250), (320, 250)]

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()

speed = 15
speed_increment = 5

while True:
    pygame.time.Clock().tick(speed)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            break
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key
            
    screen.blit(apple_surface, apple_pos)
    pygame.display.update()

    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = random_on_grid()
        speed += speed_increment

    for pos in snake_pos:
        screen.blit(snake_surface, pos)
        screen.blit(apple_surface, apple_pos)

    for i in range(len(snake_pos)-1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            # Blit the "Game Over" text to the screen
            screen.blit(gameover_text, (WINDOW_SIZE[0]/2 - 100, WINDOW_SIZE[1]/2))
            pygame.display.update()
            pygame.time.wait(3000) # wait for 3 seconds
            pygame.quit()
            quit()
        snake_pos[i] = (snake_pos[i-1])
    
    if off_limits(snake_pos[0]):
        # Blit the "Game Over" text on the screen
        screen.blit(gameover_text, (WINDOW_SIZE[0/2] - 100, WINDOW_SIZE[1/2]))
        pygame.display.update
        pygame.quit()
        quit()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    if off_limits(snake_pos2[0]):
        pygame.quit()
        quit()

    pygame.display.update()