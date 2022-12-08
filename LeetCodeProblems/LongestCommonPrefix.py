inp = ["flower", 'florist', 'flock', 'flour']

def longestCommonPrefix(strs):
        if not strs:
            return "n"
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                #The set function will remove duplicates
                #If a set has more than one item in it, 
                return strs[0][:i]
                
        else:
            return min(strs)



def LCP(inp:list):
    prefix =[]
    for i in inp:
        j=[]
        j.append([*i])
        for k in range(len(j)-1):
            if prefix is None:
                prefix = j
            if not prefix[k] or prefix[k]:
                prefix[k]



print(LCP(inp))
