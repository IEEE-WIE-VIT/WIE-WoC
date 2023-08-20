class Solution:
    def romanToInt(self, s: str) -> int:
        m={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        answer=0
        i=0
        while i<len(s)-1:
            if m[s[i]]<m[s[i+1]]:
                answer+=m[s[i+1]]-m[s[i]]
                i+=2
            else:
                answer+=m[s[i]]
                i+=1
        if i==len(s)-1:
            answer+=m[s[i]]
        return answer

sol=Solution()
