# https://zerojudge.tw/ShowProblem?problemid=a003
# a003: 兩光法師占卜術

month, day = map(int, input().split())
luck = (month * 2 + day) % 3
if luck == 0:
    print('普通')
elif luck == 1:
    print('吉')
else:
    print('大吉')
