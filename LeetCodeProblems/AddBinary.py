class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [*a]
        b = [*b]
        c=[]

        if a>b:
            lArray = a
            #Longer Array
        else:
            lArray = b

        for i in range(len(lArray),0,-1):
            c = lArray[i]



        return b,a




arr1 = "1011"
arr2 = "1010"
s = Solution()
print(s.addBinary(arr1, arr2))