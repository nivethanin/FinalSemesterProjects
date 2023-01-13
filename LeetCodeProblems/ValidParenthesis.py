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
            if len(stack)<1 or fs[i] not in self.DIC:
                stack.append(fs[i])

            elif fs[i] in self.DIC and stack[len(stack)-1] == fs[i]:
                stack.pop()
            
            else:
                return False

        
        if stack

            
        
            

g = "(]"
r = Solution()
print(r.isValid(g))

