# https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/python

def close_compare(a, b, margin=0):
    if 0 <= a - b <= margin or 0 <= b - a <= margin:
        return 0
    if a - b > margin:
        return 1
    return -1
