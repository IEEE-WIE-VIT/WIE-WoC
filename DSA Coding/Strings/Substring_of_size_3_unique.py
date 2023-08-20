def countGoodSubstrings(self, s):
        
        count = 0
        for i in range(0,len(s)-2):
            l = s[i:i+3]
            if len(l) == len(list(set(l))):
                count += 1
        return count
