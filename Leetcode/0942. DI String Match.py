# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = -1, 1
        result = [0]
        for op in s:
            if op == 'I':
                result.append(high)
                high += 1
            else:
                result.append(low)
                low -= 1

        return map(lambda x: x - low - 1, result)
