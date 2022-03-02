n = int(input())

space = 0
for i in range(n,0,-1):
    for k in range(space):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()
    space += 2
    
space -= 4
for i in range(2,n+1):
    for k in range(space):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()
    space -=2
        
        




