class Solution:
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
                    if stack.pop() == self.DIC[fs[i]]:
                        continue
                    else:
                        return False
                        #clean
                else:
                    stack.append(fs[i])
            
            else: 
                if i in self.DIC.keys() and stack.pop() != self.DIC[i]:
                    return False


        if len(stack)!=0:
            return False
        
        return True
        
g = "([)]"
r = Solution()
print(r.isValid(g))

