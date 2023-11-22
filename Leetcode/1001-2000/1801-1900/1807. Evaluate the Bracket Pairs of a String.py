# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        words = {}
        for key, word in knowledge:
            words[key] = word

        prev = index = 0
        result = []
        while index < len(s):
            while index < len(s) and s[index] != '(':
                index += 1
            result.append(s[prev:index])
            if index == len(s):
                break
            index += 1
            prev = index
            while s[index] != ')':
                index += 1
            word = s[prev:index]
            if word in words:
                result.append(words[word])
            else:
                result.append('?')
            index += 1
            prev = index
        return "".join(result)
