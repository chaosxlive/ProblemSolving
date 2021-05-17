# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(iterable):
    prevItem = None
    result = []
    for item in iterable:
        if item != prevItem:
            result.append(item)
            prevItem = item
    return result