class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = [*s]
        ref = {}
        
        pal = 0
        nums = 0

        for i in s:
            nums +=1
            if i in ref:
                ref[i] = ref[i] + 1
                if ref[i]%2 ==0:
                    pal+=2

            else:
                ref[i] = 1

        if nums == pal:
            return pal
        else:
            return pal +1


s = Solution()
print(s.longestPalindrome('aAAabbydahgjvc'))