# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        def count(word):
            counter = [0] * 26
            for c in word:
                counter[ord(c) - 97] += 1
            return tuple(counter)

        for word in strs:
            result[count(word)].append(word)

        return list(result.values())
