import pygame
from  pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0,0,0))
pygame.display.set_caption("インベーダー")


running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                screen.fill((255, 0, 0))
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                screen.fill((0, 255, 0))
        if event.type == KEYDOWN  :
            if event.key == K_UP:
                screen.fill((0, 0, 255))
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                screen.fill((0, 0, 0))








    pygame.display.update()






