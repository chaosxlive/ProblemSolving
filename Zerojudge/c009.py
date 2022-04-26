# https://zerojudge.tw/ShowProblem?problemid=c009
# c009: 10473 - Simple Base Conversion

while True:
    num = input()
    if len(num) >= 2 and num[1] == 'x':
        print(int(num, 16))
    else:
        num = int(num)
        if num >= 0:
            print('0x' + hex(num).upper()[2:])
        else:
            break
