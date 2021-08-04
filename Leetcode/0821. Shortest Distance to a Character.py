# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        occurrences = [i for i, ch in enumerate(s) if ch == c]
        result = [0] * len(s)
        for i in range(occurrences[0]):
            result[i] = occurrences[0] - i
        for i in range(1, len(occurrences)):
            for j in range(occurrences[i - 1] + 1, occurrences[i]):
                result[j] = min(j - occurrences[i - 1], occurrences[i] - j)
        for i in range(occurrences[-1] + 1, len(s)):
            result[i] = i - occurrences[-1]

        return result
