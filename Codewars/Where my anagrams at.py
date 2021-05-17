# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

def anagrams(word, words):
    countWord = {}
    for c in word:
        if c not in countWord:
            countWord[c] = 0
        countWord[c] += 1
    result = []
    for w in words:
        if len(w) != len(word):
            continue
        countW = {}
        isMatch = True
        for c in w:
            if c not in countW:
                countW[c] = 0
            countW[c] += 1
            if c not in countWord or countW[c] > countWord[c]:
                isMatch = False
                break
        if isMatch:
            result.append(w)
    return result