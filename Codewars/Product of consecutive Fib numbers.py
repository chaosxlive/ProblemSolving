# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

def productFib(prod):
    listFib = [0, 1]
    index = 0
    while True:
        product = listFib[index] * listFib[index + 1]
        if product == prod:
            return [listFib[index], listFib[index + 1], True]
        elif product > prod:
            return [listFib[index], listFib[index + 1], False]
        listFib.append(listFib[index] + listFib[index + 1])
        index += 1
