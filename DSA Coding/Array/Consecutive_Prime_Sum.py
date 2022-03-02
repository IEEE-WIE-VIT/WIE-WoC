def isPrime(num):
        i=2
        flag=0
        while(i*i <= num):
            if(num%i==0):
                flag+=1
                break
            i+=1
        if(flag==1):
            return 0
        else:
            return 1

t = int(input())

for i in range(t):
    n = int(input())
    l = []
    for k in range(2,n+1):
        if isPrime(k):
            l.append(k)
    count = 0
    sumt = 0
    nl = l[2:]
    for i in range(0,len(l)):
        sumt += l[i]
        if sumt in nl:
            count += 1
    print(count)
        
        









