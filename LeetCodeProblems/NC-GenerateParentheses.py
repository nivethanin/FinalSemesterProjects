class Solution:
    """Not Complete"""
    def isValid(self, s: str):

        ss = [*s]
        fs = []
        for i in range(len(ss)):
            if ss[i] == "(":
                fs.append(ss[i])
            elif len(fs)>0:
                fs.pop(0)
            else:
                return False
        
        if len(fs)>0:
            return False

        return True
            
            

    def generateParenthesis(self, n: int):
        l =["("] * n * 2
        print(l)
        for i in range(n):
            temp = []
            for j in range(n):
                
                for k in range(2):
                    if k % 2 == 0:
                        temp.append('(')
                    else:
                        l.append(')')

        print(l)



        


g = Solution()
# print(g.isValid("(()())()"))

g.generateParenthesis(3)