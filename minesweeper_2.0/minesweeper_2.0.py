import random, pygame, sys
from pygame.locals import *


n = 3 #size of map
mine = 3 #number of mines
count = 0
state = True #state of the game

for i in range(1,n+1):
    locals()['list_'+str(i)]=[]
    locals()['surface_'+str(i)]=[]
    locals()['number_'+str(i)]=[]
    # create list and surface

for a in range(1,n+1):
    for i in range (1,n+1):
        locals()['list_'+str(i)].append(0)
        #create list       

j = random.sample(range(1,n+1), n)
i = random.sample(range(0,n), n)
for k in range(0,mine):
    for p,q in zip(j, i):
        # print(p,q)#debug
        locals()['list_'+str(p)][q] = 1
        #plant mines

for i in range(1,n+1):
    for j in range(1,n+1):
        locals()['surface_'+str(i)].append("x")
        #initialize surface

for y in range (1,n+1):
    for x in range (0,n):
        # print(x,y)#debug
        count = 0
        if y < n :
            if locals()['list_'+str(y+1)][x] == 1:
                count += 1
        if y < n and x < n-1:
            if locals()['list_'+str(y+1)][x+1] == 1:
                count += 1
        if y < n and x > 0:
            if locals()['list_'+str(y+1)][x-1] == 1:
                count += 1
        if x < n-1:
            if locals()['list_'+str(y)][x+1] == 1:
                count += 1
        if x > 0:
            if locals()['list_'+str(y)][x-1] == 1:
                count += 1
        if y > 1:
            if locals()['list_'+str(y-1)][x] == 1:
                count += 1
        if y > 1 and x < n-1:
            if locals()['list_'+str(y-1)][x+1] == 1:
                count += 1
        if y > 1 and x > 0:
            if locals()['list_'+str(y-1)][x-1] == 1:
                count += 1
        locals()['number_'+str(y)].append(count)

pygame.init()

screen = pygame.display.set_mode((n*100,n*100))
pygame.display.set_caption('minesweeper')
block = pygame.image.load('D:\桌面\python\game\minesweeper_2.0\\block.jpg').convert()
block = pygame.transform.scale(block, (100,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
    screen.fill((0,0,0))
    for i in range(0,n):
        for j in range(0,n):
            # print(i,j)#debug
            screen.blit(block, (100*i,100*j))
    pygame.display.update()




# while True:
#     for i in range(1,n+1):
#         print("   ", i, end="")  
#     print("")
#     for i in range(1,n+1):
#         print(i, locals()['surface_'+str(i)])  
#     #print user interface

#     print("")
#     for i in range(1,n+1):
#         print(locals()['list_'+str(i)])
#     print("")
#     for i in range(1,n+1):
#         print(locals()['number_'+str(i)])
#     print("")
#     # break
#     #debug

#     x = int(input("Enter the x position"))
#     y = int(input("Enter the y position"))
#     x -= 1

#     #get user input
#     # print(x,y)
#     # print(locals()['list_'+str(y)][x])
#     # print(locals()['list_'+str(y)])
#     # #debug

#     count +=1
#             #detect if all the bombs have been found

#     if locals()['list_'+str(y)][x] == 1:
#         print("The mine exploded!")
#         break
#         #detect bomb

    
#     if count == n**2 - mine:
#         print("You win!")
#         break
#         #print winning message

#     if locals()['list_'+str(y)][x] != 1 :
#         locals()['surface_'+str(y)][x] = str(locals()['number_'+str(y)][x])
#         #change user interface
#         if y < n :
#             if locals()['number_'+str(y+1)][x] == 0:
#                 locals()['surface_'+str(y+1)][x] = str(locals()['number_'+str(y+1)][x])
#         if y < n and x < n-1:
#             if locals()['number_'+str(y+1)][x+1] == 0:
#                 locals()['surface_'+str(y+1)][x+1] = str(locals()['number_'+str(y+1)][x+1])
#         if y < n and x > 0:
#             if locals()['number_'+str(y+1)][x-1] == 0:
#                 locals()['surface_'+str(y+1)][x] = str(locals()['number_'+str(y+1)][x])
#         if x < n-1:
#             if locals()['number_'+str(y)][x+1] == 0:
#                 locals()['surface_'+str(y)][x+1] = str(locals()['number_'+str(y)][x+1])
#         if x > 0:
#             if locals()['number_'+str(y)][x-1] == 0:
#                 locals()['surface_'+str(y)][x-1] = str(locals()['number_'+str(y)][x-1])
#         if y > 1:
#             if locals()['number_'+str(y-1)][x] == 0:
#                 locals()['surface_'+str(y-1)][x] = str(locals()['number_'+str(y-1)][x])
#         if y > 1 and x < n-1:
#             if locals()['number_'+str(y-1)][x+1] == 0:
#                 locals()['surface_'+str(y-1)][x+1] = str(locals()['number_'+str(y-1)][x+1])
#         if y > 1 and x > 0:
#             if locals()['number_'+str(y-1)][x-1] == 0:
#                 locals()['surface_'+str(y-1)][x-1] = str(locals()['number_'+str(y-1)][x-1])
#         #detect any zeros around the coordinate
