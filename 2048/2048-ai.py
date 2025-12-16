import pygame
from random import choice as c
import colorsys
from math import tanh
from copy import deepcopy

SIZE = 4 # no change
B_S = 120
S_W = B_S*SIZE
S_H = B_S*SIZE
FPS = 100

def can_combine(a,b):
    if a == b: return True
    return False
def operate(a,b):
    return a+b
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
def rand():
    return c([1,2,3,4,5,6,7,8,9,0])
def how_good(grid): # how good is playing
    out = 0
    largest = float("inf")
    cnt = 0
    for i,j in enumerate([(0,3),(1,3),(2,3),(3,3),(3,2),(2,2),(1,2),(0,2),(0,1),(1,1),(2,1),(3,1),(3,0),(2,0),(1,0),(0,0)]):
        x,y = j
        if grid[y][x] == None:
            cnt += 1
            return out
        if grid[y][x] <= largest:
            largest = grid[y][x]
            out += 2**(16-i)*grid[y][x]
        else: return out
    return out
def how_good_search(grid,layer): # grid is a object # 深度搜索<layer>层
    layer -= 1
    if layer == 0:
        return how_good(grid.grid)
    else:
        points = [0,0,0,0]
        for i,direction in enumerate("wasd"):
            grid.move_combine(direction)
            total = []
            if grid.grid != grid.prev:
                '''for xy in grid.empty:
                    new_grid = deepcopy(grid)
                    new_grid.spawn(xy)
                    total.append(how_good_search(new_grid,layer))
                out = 0
                outlen = 0
                for j in total:
                    if j != 0:
                        out += j
                        outlen += 1
                points[i] = out/outlen'''
                points[i] = how_good(grid.grid)
            else: points[i] = -1
            grid.grid = deepcopy(grid.prev)
            grid.empty = grid.prevempty.copy()
        return max(points)
class grid(object):
    def __init__(self,grid=None):
        if grid == None:
            self.grid = [[None for x in range(4)] for y in range(4)]
            self.empty = {(x,y) for x in range(4) for y in range(4)}
        else:
            self.empty = set()
            for y in range(4):
                for x in range(4):
                    if self.grid[y][x] == None: self.empty.add((x,y))
        self.size = 4
    def spawn(self,xy=None):
        try:
            if xy == None:
                x,y = c(list(self.empty)) # xy for next pos
                self.empty.remove((x,y))
                self.grid[y][x] = 2
            else:
                x,y = xy # xy for next pos
                self.empty.remove((x,y))
                self.grid[y][x] = 2
        except:
            print("lose")
    def move(self,direction):
        if direction == "w":
            for x in range(self.size):
                most = 0 # upmost
                for y in range(self.size):
                    if self.grid[y][x] != None:
                        temp = self.grid[y][x]
                        self.grid[y][x] = None
                        self.empty.add((x,y))
                        self.grid[most][x] = temp
                        self.empty.remove((x,most))
                        most += 1
        elif direction == "a":
            for y in range(self.size):
                most = 0 # leftmost
                for x in range(self.size):
                    if self.grid[y][x] != None:
                        temp = self.grid[y][x]
                        self.grid[y][x] = None
                        self.empty.add((x,y))
                        self.grid[y][most] = temp
                        self.empty.remove((most,y))
                        most += 1
        elif direction == "s":
            for x in range(self.size):
                most = self.size-1 # downmost
                for y in range(self.size-1,-1,-1):
                    if self.grid[y][x] != None:
                        temp = self.grid[y][x]
                        self.grid[y][x] = None
                        self.empty.add((x,y))
                        self.grid[most][x] = temp
                        self.empty.remove((x,most))
                        most -= 1
        elif direction == "d":
            for y in range(self.size):
                most = self.size-1 # rightmost
                for x in range(self.size-1,-1,-1):
                    if self.grid[y][x] != None:
                        temp = self.grid[y][x]
                        self.grid[y][x] = None
                        self.empty.add((x,y))
                        self.grid[y][most] = temp
                        self.empty.remove((most,y))
                        most -= 1
    def combine(self,direction):
        if direction == "w":
            for x in range(self.size):
                for y in range(self.size-1):
                    if self.grid[y+1][x] != None:
                        if can_combine(self.grid[y][x],self.grid[y+1][x]):
                            self.grid[y][x] = operate(self.grid[y][x],self.grid[y+1][x])
                            self.grid[y+1][x] = None
                            self.empty.add((x,y+1))
        elif direction == "a":
            for y in range(self.size):
                for x in range(self.size-1):
                    if self.grid[y][x+1] != None:
                        if can_combine(self.grid[y][x],self.grid[y][x+1]):
                            self.grid[y][x] = operate(self.grid[y][x],self.grid[y][x+1])
                            self.grid[y][x+1] = None
                            self.empty.add((x+1,y))
        elif direction == "s":
            for x in range(self.size):
                for y in range(self.size-1,0,-1):
                    if self.grid[y-1][x] != None:
                        if can_combine(self.grid[y][x],self.grid[y-1][x]):
                            self.grid[y][x] = operate(self.grid[y][x],self.grid[y-1][x])
                            self.grid[y-1][x] = None
                            self.empty.add((x,y-1))
        elif direction == "d":
            for y in range(self.size):
                for x in range(self.size-1,0,-1):
                    if self.grid[y][x-1] != None:
                        if can_combine(self.grid[y][x],self.grid[y][x-1]):
                            self.grid[y][x] = operate(self.grid[y][x],self.grid[y][x-1])
                            self.grid[y][x-1] = None
                            self.empty.add((x-1,y))
    def move_combine(self,direction):
        self.prev = deepcopy(self.grid)
        self.prevempty = self.empty.copy()
        self.move(direction)
        self.combine(direction)
        self.move(direction)
        if self.grid == self.prev: return -1
    def ai(self):
        points = [0,0,0,0]
        for i,direction in enumerate("wasd"):
            self.move_combine(direction)
            if self.grid != self.prev:
                points[i] = how_good_search(deepcopy(self),2)
                #print(self.grid)
            else: points[i] = -1
            self.grid = deepcopy(self.prev)
            self.empty = self.prevempty.copy()
        # print(points)
        return "wasd"[points.index(max(points))]
    def draw(self):
        for i in self.grid:
            for j in i:
                if j == None:
                    print(" "*4,end="|")
                else: print(str(j).ljust(4," "),end="|")
            print()
            
class world(object):
    def __init__(self):
        self.size = SIZE # kegai
        self.grid = grid()
        self.mode = 0
    def get_direction_move(self):
        #keys = pygame.key.get_pressed()
        direction = self.grid.ai()
        #if keys[pygame.K_w]: direction = "w"
        #elif keys[pygame.K_a]: direction = "a"
        #elif keys[pygame.K_s]: direction = "s"
        #elif keys[pygame.K_d]: direction = "d"
        if direction != None:
            #print(direction)
            if self.grid.move_combine(direction) != -1:
                self.grid.spawn()
        self.draw()
        #print(how_good(self.grid.grid))
    def test_over(self):
        pass #gai
    def game_over(self):
        pass #gai
    def draw(self):
        screen.fill((255,255,255))
        for y,i in enumerate(self.grid.grid):
            for x,j in enumerate(i):
                if j != None:
                    FONT = pygame.font.Font('arial.ttf', round((B_S/len(str(j)))))
                    text = FONT.render(str(j),True,hsv2rgb((tanh(j/100)+0.2)%1,1,1))
                    text_rect = text.get_rect()
                    text_rect.center = (B_S*x+B_S//2,B_S*y+B_S//2)
                    screen.blit(text,text_rect)

pygame.init()
FONT = pygame.font.Font('arial.ttf', B_S//3)
screen=pygame.display.set_mode((S_W, S_H))
scr = pygame.Surface((S_W, S_H))
clock = pygame.time.Clock()
pygame.display.set_caption("2048")
w = world()
w.grid.spawn()
w.draw()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quit pygame
            running = False
        if event.type == pygame.KEYDOWN:
            w.get_direction_move()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_0]: w.mode += 1
    w.get_direction_move()
    pygame.display.update()
pygame.quit()
    

