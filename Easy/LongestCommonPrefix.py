def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    currentMaxPrefix = ""
    
    if len(strs) == 1:
        return strs[0]
    
    for char in range(0,min([len(x) for x in strs])):
        currentSet = set()
        for word in strs:
            currentSet.add(word[char])

        if len(currentSet) != 1:
            return currentMaxPrefix
        else:
            currentMaxPrefix += list(currentSet)[0]

    return currentMaxPrefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))