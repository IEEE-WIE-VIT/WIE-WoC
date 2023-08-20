n = str(int(input()))
F = []
Flag = False


def fibonacci(a):
    x = 0
    y = 1
    z = 0
    while z <= a:
        z = x + y
        x = y
        y = z
        if z == a:
            return True


for length in range(1, (len(n)+1)):
    for i in range(0, (len(n)-length+1)):
        Flag = fibonacci(int(n[i:(i+length)]))
        if Flag:
            if int(n[i:(i+length)]) in F:
                continue
            else:
                F.append(int(n[i:(i+length)]))
F.sort()
if F == []:
    print("None")
else:
    for i in range(len(F)):
        print(F[i])

