def maxArr(self, A):
        
        mx = -10000000000
        for i in range(len(A)):
            for j in range(len(A)):
                res = abs(A[i]-A[j])+abs(i-j)
                if res > mx:
                    mx = res
        return mx
