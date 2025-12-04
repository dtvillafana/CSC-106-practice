import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")
BLACK = (0,0,0)
WHITE = (255,255,255)
clock = pygame.time.Clock()
FPS = 60

rect = (100, 100, 200, 150)
running = True

def move_rectangle(tup):
    if tup[0] > WIDTH or tup[1] > HEIGHT:
        return (0,0, tup[2], tup[3])
    else:
        return (tup[0] + 1, tup[1] + 1, tup[2], tup[3])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, rect)
    rect = move_rectangle(rect)



    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
