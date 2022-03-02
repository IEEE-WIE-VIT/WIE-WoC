num = int(input())
for i in range(num):
    print("*",end=" ")
print()

k = 1
sp = 2*num-5
for i in range(num-1):
    for _ in range(k):
        print("",end=" ")
    k=k+1
    print('*',end='')
    if i != num-2:
        for _ in range(sp):
            print("",end=" ")
        sp = sp-2
        print('*',end='')
    print()
    



