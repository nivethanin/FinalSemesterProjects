class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """ Commented out section was original thought process"""

        m=len(haystack)
        n=len(needle)

        for i in range(m):

            if haystack[i:i+n]==needle:
                return i

        return -1




        # hs = [*haystack]
        # nd = [*needle]

        # if nd[0] not in hs:
        #     return -1
        
        
        # ndCount = 0
  
        # for i in range(len(hs)):
            
        #     if hs[i] == nd[ndCount]:
        #         ndCount +=1

        #         if ndCount==len(nd):
        #             return i-ndCount+1


        #     elif hs[i] == nd[0]:
        #         ndCount = 1
                
        #     else:
        #         ndCount = 0

        # return -1


s = Solution()

print(s.strStr("mississippi", "issip"))