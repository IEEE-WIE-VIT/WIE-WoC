class Solution:
    def longestCommonPrefix(self, A):        
        prefix = A[0]
        n = len(prefix)
        
        for i in range(len(A)):
            while(prefix not in A[i]):
                n = n-1
                prefix = prefix[:n]
            
        return prefix
