# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    numbers.strip(' ')
    numMax, numMin = -2147483648, 2147483647
    for number in numbers.split(' '):
        if int(number) > numMax:
            numMax = int(number)
        if int(number) < numMin:
            numMin = int(number)
    return str(numMax) + " " + str(numMin)