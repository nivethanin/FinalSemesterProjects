class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [*s]
        t = [*t]
        if len(s) != len(t):
            return False

        ldb = {}
        for i in range(len(t)):
            """ This is to add the letters from word t into the dictionary"""
            if t[i] not in ldb:
                ldb.update({t[i]:1})
            else:
                num = ldb[t[i]]
                ldb.update({t[i]:num+1})
        
        print(ldb)
        
        for i in range(len(s)):
            if s[i] in t:
                num = ldb[s[i]] - 1
                ldb.update({s[i]:num})
                if num<0:
                    return False
            else:
                return False
        return True

sol = Solution()

print(sol.isAnagram("aacc", "ccac"))