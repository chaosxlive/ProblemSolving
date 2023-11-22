# https://leetcode.com/problems/count-common-words-with-one-occurrence/

from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)

        result = 0

        for key, count in counter1.items():
            if count == 1 and counter2[key] == count:
                result += 1

        return result
