n = int(input())

space = 0
for j in range(n,0,-1):
    for k in range(space):
        print(' ',end='')
    for i in range(j):
        print('*',end=" ")
    space +=1
    print()
    




