def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    table = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    value = 0

    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

    for x in s:
        value += table[x]

    return value

print(romanToInt("LVIII"))