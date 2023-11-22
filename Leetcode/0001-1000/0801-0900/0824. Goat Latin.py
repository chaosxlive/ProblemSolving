# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        isVowelStart = False
        charStart = ''
        count = 1
        isStart = True
        index = 0
        while index < len(sentence):
            if isStart:
                isStart = False
                if sentence[index] in "AEIOUaeiou":
                    result.append(sentence[index])
                    isVowelStart = True
                else:
                    isVowelStart = False
                    charStart = sentence[index]
            elif sentence[index] == ' ':
                if not isVowelStart:
                    result.append(charStart)
                result.append("ma")
                result.append("a" * count)
                result.append(" ")
                isStart = True
                count += 1
            else:
                result.append(sentence[index])
            index += 1
        if not isVowelStart:
            result.append(charStart)
        result.append("ma")
        result.append("a" * count)
        return "".join(result)
