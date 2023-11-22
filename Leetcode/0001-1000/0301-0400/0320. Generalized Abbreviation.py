# https://leetcode.com/problems/generalized-abbreviation/

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []
        if len(word) == 1:
            return ["1", word]

        def func(current, rest, isNum):
            if len(rest) == 0:
                result.append(current)
                return
            for l in range(1, len(rest) + 1):
                if isNum:
                    func(current + str(l), rest[l:], False)
                else:
                    func(current + rest[:l], rest[l:], True)

        func("", word, True)
        func("", word, False)
        return result
