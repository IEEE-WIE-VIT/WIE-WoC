n = int(input())

space = n-1

for i in range(n):
    for k in range(space):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
    space -= 1



