n = int(input())
d = 0
pairs = 0


def factors(a, b):
    la = []
    lb = []
    for counter in range(2, a):
        if a%counter == 0:
            la.append(counter)
    for counter in range(2, b):
        if b%counter == 0:
            lb.append(counter)
    if len(la) == len(lb):
        return True
    return False


for counter in range(1, (int(n/2)+1)):
    if n%counter == 0 and counter < n//counter:
        pairs += 1
        Flag1 = factors(counter, n//counter)
        if Flag1:
            d += 1
if pairs > 0:
    print(d)
else:
    print(-1)
