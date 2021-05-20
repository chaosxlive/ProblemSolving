# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(n):
    result = 0
    while n >= 10:
        temp = 1
        while n > 0:
            temp *= n % 10
            n //= 10
        n = temp
        result += 1
    return result
