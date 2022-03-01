n = int(input())
l1 = []; l2 = []
dummy = n
counter = 0
while dummy > 0:
    dummy //= 10
    counter += 1
dummy = n; i = 0
if counter%2==0:
    while dummy > 0:
        if i%2==0:
            l1.append(dummy%10)
        else:
            l2.append(dummy%10)
        i += 1
        dummy //= 10
print(abs(sum(l1) - sum(l2)))
