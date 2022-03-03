class Solution:
    def reverseWords(self,S):
        # code here 
        l = S.split('.')
        st = ''
        for i in range(len(l)-1,-1,-1):
            st += l[i] + '.'
           
        return st[:len(st)-1]
