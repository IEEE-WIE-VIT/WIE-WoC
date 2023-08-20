def rotate(self, a):        
        #transpose
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                a[i][j],a[j][i] = a[j][i],a[i][j]
        
        #reverse each row
        for l in a:
            l.reverse()
        return a
