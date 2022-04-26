# https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 1
        while True:
            if (word * count in sequence):
                count += 1
            else:
                return count - 1
