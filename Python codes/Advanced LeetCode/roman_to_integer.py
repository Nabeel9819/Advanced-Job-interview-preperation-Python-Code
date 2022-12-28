roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
s = "IXM"
result = 0
if 1 <= len(s) <= 15:
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            result = result - roman[s[i]]
        else:
            result = result + roman[s[i]]
print(result)