import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600))
Image = pygame.image.load("./pic/yellow.jpg")
Rect = Image.get_rect()
Rect.center = (400, 300)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(Image, Rect)
    pygame.display.update()