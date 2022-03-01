n = int(input())
m = int(input())
boolean2 =False
for i in range(2,m+1):
    boolean1 = True
    for j in range((10**(n-1)),(10**n)):
        j = j * ((10**n) + 1)
        if (j%i!=0):
            boolean1 = False
            break
    if boolean1 == True:
        print(i)
        boolean2 = True
if boolean2 == False:
    print('No complete factors')
