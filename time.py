import pygame
import time
import pygame.freetype
from pygame.locals import *
import sys
import random

blue = (102,204,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("时间")
text = pygame.freetype.SysFont("fangsong", 32)
text1 = pygame.freetype.SysFont("fangsong", 16)


while True:
    var = time.asctime()
    screen.fill(black)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    textrect = text.render_to(screen, (200,300), var, fgcolor=(r,g,b))
    textrect = text1.render_to(screen, (200,350), "Press esc to quit", fgcolor=(225,225,255))
    pygame.display.update()
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
