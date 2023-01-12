class Solution:
    """ The rules of this problem have changed """

    DIC = {
        "}":"{" ,
        "]":"[" ,
        ")":"("
    }


    def isValid(self, s:str):
        stack =[]
        fs = [*s]

        """Could add case for starting with open brackets"""

        for i in range(len(fs)):
            if len(stack)<1:
                stack.append(fs)
            
        
            

g = "(]"
r = Solution()
print(r.isValid(g))

