# https://www.codewars.com/kata/586ee462d0982081bf001f07/train/python

def fillable(stock, merch, n):
    return not (merch not in stock or stock[merch] < n)
