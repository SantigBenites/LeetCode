
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    import math
    strX = str(x)
    size = len(strX)
    stack = []
    bool = True

    for i in range(int(len(strX)/2)):
        strX, result = strX[:-1], strX[-1]
        stack.append(result)

    if size % 2 == 1:
        strX, result = strX[:-1], strX[-1]

    for i in strX:
        strX, result = strX[:-1], strX[-1]
        bool = bool and (result == stack.pop())

    return bool


x = 121
print(isPalindrome(x))