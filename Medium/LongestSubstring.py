def lengthOfLongestSubstring( s):

    if len(s) == 1:
        return s
    
    l = 0
    max_len = 0
    foundChars = []


s = "dvdf"
print(lengthOfLongestSubstring(s))