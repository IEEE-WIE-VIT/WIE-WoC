class Solution:
    def romanToInt(self, s):
        
        s = str(s)
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
          
          
        num = 0
        i = 0
         
        while i < len(s)-1:
            if i+1 < len(s)-1 and roman[s[i+1]] > roman[s[i]]  :
                num -= roman[s[i]]
            else:
                num+=roman[s[i]]
            i+=1
        return num


