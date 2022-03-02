def Fac(self, n):        
        if(n==0):
            return 1 # base case
        else:
            return( n * self.Fac(n-1) )  # recursive case
