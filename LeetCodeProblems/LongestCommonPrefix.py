inp = ["flower", 'florist', 'flock']

def longestCommonPrefix( strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            print(f" {i} and letter group is {letter_group}")
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


longestCommonPrefix(inp)