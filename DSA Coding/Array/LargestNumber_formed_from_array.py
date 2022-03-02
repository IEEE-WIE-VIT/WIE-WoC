def largestNumber(self, a):  
        
        largestnumber =''
        for i in range(len(a)-1):
            for j in range(i+1, len(a)):
                string1 = str(a[i])+str(a[j])
                string2 = str(a[j])+str(a[i])
                if int(string2) > int(string1):
                    a[i] , a[j] = a[j] , a[i]
        for i in range(len(a)):
            largestnumber += str(a[i])
        return int(largestnumber)
