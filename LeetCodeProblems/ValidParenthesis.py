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
        for i in range(len(fs)):
            
            if len(stack)>0: 
                if fs[i] in self.DIC.keys():
                    if stack[len(stack)] == self.DIC[fs[i]]:
                        stack.pop()
                        continue
                    else:
                        return False
                        #clean
                else:
                    stack.append(fs[i])
            
            else: 
                print("i'm here")
                print(stack[len(stack)])
                if i in self.DIC.keys() and stack[len(stack)] != self.DIC[i]:
                    return False

        if len(stack)>0:
            return False

        return True

g = "(]"
r = Solution()
print(r.isValid(g))

