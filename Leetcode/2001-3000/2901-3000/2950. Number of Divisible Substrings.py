# https://leetcode.com/problems/number-of-divisible-substrings/

from itertools import accumulate


class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        m = {
            'a': 1, 'b': 1,
            'c': 2, 'd': 2, 'e': 2,
            'f': 3, 'g': 3, 'h': 3,
            'i': 4, 'j': 4, 'k': 4,
            'l': 5, 'm': 5, 'n': 5,
            'o': 6, 'p': 6, 'q': 6,
            'r': 7, 's': 7, 't': 7,
            'u': 8, 'v': 8, 'w': 8,
            'x': 9, 'y': 9, 'z': 9,
        }

        arr = list(map(lambda x: m[x], word))
        acc = [0] + list(accumulate(arr))
        result = 0
        for l in range(1, len(arr) + 1):
            for i in range(len(arr) - l + 1):
                if (acc[i + l] - acc[i]) % l == 0:
                    result += 1
        return result
