# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def isLetterLog(log: str):
            index = 0
            while log[index] != ' ':
                index += 1
            index += 1
            return 'a' <= log[index] <= 'z'

        resultLetter, resultDigit = [], []
        for log in logs:
            if isLetterLog(log):
                resultLetter.append(log)
            else:
                resultDigit.append(log)
        return sorted(resultLetter, key=lambda x: (x[x.index(' ') + 1:], x[:x.index(' ')])) + resultDigit
