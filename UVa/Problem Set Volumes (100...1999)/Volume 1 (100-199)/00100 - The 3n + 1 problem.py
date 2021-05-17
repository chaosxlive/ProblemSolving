history = {1: 1}


def find3nP1(n):
    global history

    if n not in history:
        if n % 2 == 0:
            history[n] = find3nP1(n // 2) + 1
        else:
            history[n] = find3nP1(3 * n + 1) + 1
    return history[n]


while True:
    try:
        input1, input2 = map(int, input().split(' ')[:2])
        maxCount = 0
        for i in range(min(input1, input2), max(input1, input2) + 1):
            temp = find3nP1(i)
            if temp > maxCount:
                maxCount = temp
        print(f'{input1} {input2} {maxCount}')
    except EOFError:
        break
