import random

n = 10 #size of map
mine = 10 #number of mines
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

# j = random.sample(range(1,n+1), n)
# i = random.sample(range(0,n), n)
# for k in range(0,mine):
#     p = j[k]
#     q = i[k]
#     print(p,q)#debug
#     locals()['list_'+str(p)][q] = 1
#     #plant mines

check = []
check_1 = []

while True:
    p = random.randint(1,n)
    q = random.randint(0,n-1)
    # print(p,q)
    if p not in check and q not in check_1:
        check.append(p)
        check_1.append(q)
        # print(p,q)
        locals()['list_'+str(p)][q] = 1
        mine -= 1
        # print(mine)
    elif mine == 0:
        break
    
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

while True:
    for i in range(1,n+1):
        print("   ", i, end="")  
    print("")
    for i in range(1,n+1):
        print(i, locals()['surface_'+str(i)])  
    #print user interface

    print("")
    for i in range(1,n+1):
        print(locals()['list_'+str(i)])
    print("")
    for i in range(1,n+1):
        print(locals()['number_'+str(i)])
    print("")
    # break
    #debug

    x = int(input("Enter the x position"))
    y = int(input("Enter the y position"))
    x -= 1

    #get user input
    # print(x,y)
    # print(locals()['list_'+str(y)][x])
    # print(locals()['list_'+str(y)])
    # #debug

    count +=1
            #detect if all the bombs have been found

    if locals()['list_'+str(y)][x] == 1:
        print("The mine exploded!")
        break
        #detect bomb

    
    if count == n**2 - mine:
        print("You win!")
        break
        #print winning message

    if locals()['list_'+str(y)][x] != 1 :
        locals()['surface_'+str(y)][x] = str(locals()['number_'+str(y)][x])
        #change user interface
        if y < n :
            if locals()['number_'+str(y+1)][x] == 0:
                locals()['surface_'+str(y+1)][x] = str(locals()['number_'+str(y+1)][x])
        if y < n and x < n-1:
            if locals()['number_'+str(y+1)][x+1] == 0:
                locals()['surface_'+str(y+1)][x+1] = str(locals()['number_'+str(y+1)][x+1])
        if y < n and x > 0:
            if locals()['number_'+str(y+1)][x-1] == 0:
                locals()['surface_'+str(y+1)][x] = str(locals()['number_'+str(y+1)][x])
        if x < n-1:
            if locals()['number_'+str(y)][x+1] == 0:
                locals()['surface_'+str(y)][x+1] = str(locals()['number_'+str(y)][x+1])
        if x > 0:
            if locals()['number_'+str(y)][x-1] == 0:
                locals()['surface_'+str(y)][x-1] = str(locals()['number_'+str(y)][x-1])
        if y > 1:
            if locals()['number_'+str(y-1)][x] == 0:
                locals()['surface_'+str(y-1)][x] = str(locals()['number_'+str(y-1)][x])
        if y > 1 and x < n-1:
            if locals()['number_'+str(y-1)][x+1] == 0:
                locals()['surface_'+str(y-1)][x+1] = str(locals()['number_'+str(y-1)][x+1])
        if y > 1 and x > 0:
            if locals()['number_'+str(y-1)][x-1] == 0:
                locals()['surface_'+str(y-1)][x-1] = str(locals()['number_'+str(y-1)][x-1])
        #detect any zeros around the coordinate
