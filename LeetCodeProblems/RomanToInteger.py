class Solution:

    DIC = {
        'I':1, 
        'V':5, 
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }

    def romanToInt(self, s: str) -> int:
        total = 0
        stri = [*s]
        print(stri)
        temp = 0
        for i in range(len(stri)):
            if temp < self.DIC[stri[i]]:
                total -= temp*2
            
            total += self.DIC[stri[i]]
            
            temp = self.DIC[stri[i]]
        
        print(total)


s = Solution()
s.romanToInt('IV')

