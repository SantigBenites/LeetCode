def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    digits.reverse()
    carry = 1
    
    for x in range(0,len(digits)):
        newDigit = digits[x] + carry
        digits[x] = (newDigit) % 10
        carry = 1 if newDigit >= 10 else 0

    if carry > 0:
        digits.append(carry)
    digits.reverse()
    return digits



digits = [4,3,2,1]
print(plusOne(digits))