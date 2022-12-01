# https://leetcode.com/problems/minimum-unique-word-abbreviation/

class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:

        def generateAbbreviations(word):
            result = set()
            if len(word) == 1:
                return set([("1", 1), (word, 1)])

            def func(current, rest, isNum, step):
                if len(rest) == 0:
                    result.add((current, step))
                    return
                for l in range(1, len(rest) + 1):
                    if isNum:
                        func(current + str(l), rest[l:], False, step + 1)
                    else:
                        func(current + rest[:l], rest[l:], True, step + l)

            func("", word, True, 0)
            func("", word, False, 0)
            return result

        t = generateAbbreviations(target)
        for word in dictionary:
            w = generateAbbreviations(word)
            t.difference_update(w)

        result = (target, len(target))
        for abbr in t:
            if abbr[1] < result[1]:
                result = abbr
        return result[0]
