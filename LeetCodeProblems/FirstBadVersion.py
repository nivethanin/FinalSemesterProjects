def isBadVersion(x):
    arr = [0,1,2,-1,-1,-1]

    if arr[x]<0: 
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        rig = n
        lef = 0
        mid = 0
        
        while lef<rig:
            print(rig)

            mid = (lef + rig) // 2

            if isBadVersion(int(mid)):
                rig = mid

            else:
                lef = mid+1

        return lef


s = Solution()
print(s.firstBadVersion(5))
            