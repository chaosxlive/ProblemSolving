# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

def solution(args):
    def peekNext(arr, index):
        if index + 1 < len(arr):
            return arr[index + 1]
        else:
            return None
    index = 0
    result = ""
    while index < len(args):
        result += str(args[index])
        if peekNext(args, index) == args[index] + 1 and peekNext(args, index + 1) == args[index] + 2:
            result += "-"
            while peekNext(args, index) == args[index] + 1:
                index += 1
            result += str(args[index])
        if index < len(args) - 1:
            result += ','
        index += 1
    return result
