# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnts = [0] * 26
        for c in s:
            cnts[ord(c) - 97] += 1
        for c in t:
            cnts[ord(c) - 97] -= 1
        return all(map(lambda x: x == 0, cnts))
