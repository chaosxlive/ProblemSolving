# https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python

def encode_rail_fence_cipher(string, n):
    result = [[] for h in range(n)]
    isDown = True
    currentH = 0
    for c in string:
        result[currentH].append(c)
        if isDown:
            if currentH == n - 1:
                isDown = False
                currentH -= 1
            else:
                currentH += 1
        else:
            if currentH == 0:
                isDown = True
                currentH += 1
            else:
                currentH -= 1
    return "".join(["".join(result[h]) for h in range(n)])


def decode_rail_fence_cipher(string, n):
    indice = [[] for h in range(n)]
    isDown = True
    currentH = 0
    for index in range(len(string)):
        indice[currentH].append(index)
        if isDown:
            if currentH == n - 1:
                isDown = False
                currentH -= 1
            else:
                currentH += 1
        else:
            if currentH == 0:
                isDown = True
                currentH += 1
            else:
                currentH -= 1
    indice = [item for row in indice for item in row]
    result = [None] * len(string)
    for i in range(len(string)):
        result[indice[i]] = string[i]
    return "".join(result)
