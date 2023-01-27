class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()

        s = [*s]
        j = len(s)

        print(s)
        for i in range(len(s)):
            j-=1
            
            if j <= i:
                print("i'm here")
                return True

            if s[i] != s[j]:
                return False
            
        return True


s = Solution()

print(s.isPalindrome("lplplpra Ce CaRplplpl"))

