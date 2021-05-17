# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

import math


def find_next_square(sq):
    numSqrt = math.sqrt(sq)
    num = int(numSqrt)
    if num * num != sq:
        return -1
    return (num + 1) * (num + 1)
