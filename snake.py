import pygame
import sys
from pygame.locals import *
import pygame.freetype
import random
import time

#位置信息
head=[100,0]
snake=[
    [100,0],[80,0],[60,0]
]
x = random.randint(1,42)*20
y = random.randint(1,28)*20
x1 = random.randint(1,42)*20
y1 = random.randint(1,28)*20
x2 = random.randint(1,42)*20
y2 = random.randint(1,28)*20
food=[x,y]
food1=[x1,y1]
food2=[x2,y2]
socer=0
iseat=False
iseat1=False
iseat2=False
isover=False
goahead="R"

blue = (102,204,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
 
pygame.init()
 
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption("贪吃蛇")
 
clock = pygame.time.Clock()

while True:
    screen.fill(black)
    f1 = pygame.freetype.SysFont("fangsong", 24)

    text = pygame.freetype.SysFont("fangsong", 32)
    text1 = pygame.freetype.SysFont("fangsong", 16)


    f1rect = f1.render_to(screen, (860,20), "得分："+str(socer), fgcolor=(225,225,225))

    textrect = text1.render_to(screen, (10,10), "Press esc to quit", fgcolor=(225,225,255))

    for i in snake:
        pygame.draw.rect(screen, blue, (i[0],i[1], 20, 20))
    pygame.draw.rect(screen, red, (food[0],food[1] , 20, 20))
    pygame.draw.rect(screen, red, (food1[0],food1[1] , 20, 20))
    pygame.draw.rect(screen, red, (food2[0],food2[1] , 20, 20))
    pygame.display.update()
    clock.tick(15)

    if(goahead == "R"):
        head[0]+=20
    elif(goahead=="L"):
        head[0]-=20
    elif(goahead=="U"):
        head[1]-=20
    elif(goahead=="D"):
        head[1]+=20

    # 监听事件：键盘 鼠标 窗口退出事件
    for event in pygame.event.get():
        # 退出
        if event.type == QUIT:
            pygame.QUIT
            sys.exit()
        # 键盘按下
        if event.type==pygame.KEYDOWN:
            # 转向
            if event.key == pygame.K_LEFT:
                if (goahead=="D" or goahead=="U"):
                    goahead="L"
            elif event.key == pygame.K_RIGHT:
                if (goahead=="D" or goahead=="U"):
                    goahead="R"
            elif event.key == pygame.K_UP:
                if (goahead=="L" or goahead=="R"):
                    goahead="U"
            elif event.key == pygame.K_DOWN:
                if (goahead=="L" or goahead=="R"):
                    goahead="D"
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
    snake.insert(0, list(head))
    # 验证食物是否被吃
    if(food==head):
        iseat=True
        socer+=5
    elif(food1==head):
        iseat1=True
        socer+=5
    elif(food2==head):
        iseat2=True
        socer+=5
    # 抛出上一个位置
    elif(goahead!="T"):
        snake.pop()
    
    # 食物随机出现
    # 随机在重复位置
    if(iseat==True):
        while True:
            insnake=True
            food[0]=random.randint(1,42)*20
            food[1]=random.randint(1,28)*20
            for i in snake:
                if(food==i):
                    insnake=False
            if(insnake):
                break
        iseat=False
    if(iseat1==True):
        while True:
            insnake=True
            food1[0]=random.randint(1,42)*20
            food1[1]=random.randint(1,28)*20
            for i in snake:
                if(food==i):
                    insnake=False
            if(insnake):
                break
        iseat1=False
    if(iseat2==True):
        while True:
            insnake=True
            food2[0]=random.randint(1,42)*20
            food2[1]=random.randint(1,28)*20
            for i in snake:
                if(food==i):
                    insnake=False
            if(insnake):
                break
        iseat2=False
    # 自杀
    for i in snake[1:]:
        if(head==i):
            isover=True

    if(head[0]>1000 or head[0]<0 or head[1]>600 or head[1]<0):
        isover=True
    
    if(isover):
        f2=pygame.freetype.SysFont("arial",72)
        f2.render_to(screen,(350,150),"Game Over",fgcolor=(150,150,150))
        # 更新当前画面
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()