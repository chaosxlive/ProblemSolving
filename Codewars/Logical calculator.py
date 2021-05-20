# https://www.codewars.com/kata/57096af70dad013aa200007b/train/python

def logical_calc(array, op):
    if op == 'AND':
        for logic in array:
            if not logic:
                return False
        return True
    elif op == 'OR':
        for logic in array:
            if logic:
                return True
        return False
    else:
        result = array[0]
        for logic in array[1:]:
            result ^= logic
        return result
