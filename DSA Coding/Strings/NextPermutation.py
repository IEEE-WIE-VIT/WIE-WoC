def nextPermutation(self, a):
         
        n=len(a)
        t=n
        if(a[0]==max(a)):
            if(a[n-1]==min(a)):
                        i=0
                        while(i<=(t-(i+1))):
                            a[i],a[t-(i+1)]=a[t-(i+1)],a[i]
                            i=i+1
            else:
                a[n-1],a[n-2]=a[n-2],a[n-1]
        else:
            i=n-1
            g=0
            while(i>=0):
                if(a[i-1]<a[i]):
                    g=1
                    k=i-1
                    break
                i=i-1
            if(g==1):
                
                for i in range(n):
                    for j in range(k+1, n-i-1):
                        if int(a[j]) > int(a[j+1]) : 
                            a[j], a[j+1] = a[j+1], a[j] 
                j=k+1
                while(1):
                    if(a[k]<a[j]):
                        p=j
                        break
                    j=j+1
                a[k],a[p]=a[p],a[k]
               
            
    
