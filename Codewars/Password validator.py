# https://www.codewars.com/kata/56a921fa8c5167d8e7000053/train/python

def password(string):
    if len(string) < 8:
        return False
    hasUpper = hasLower = hasNum = False
    for c in string:
        if 'a' <= c <= 'z':
            hasUpper = True
        elif 'A' <= c <= 'Z':
            hasLower = True
        elif '0' <= c <= '9':
            hasNum = True
    return hasUpper and hasLower and hasNum