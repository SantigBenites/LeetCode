def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    map   = {")":"(","]":"[","}":"{"}
    
    for char in s:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        elif char == ")" or char == "]" or char == "}":
            if len(stack) == 0:
                return False
            latestBracket = stack.pop()
            if map[char] != latestBracket:
                return False
        else:
            return False

    return len(stack) == 0
        

s = "()"
print(isValid(s))