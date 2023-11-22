# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from bisect import bisect_left


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(set(letters))
        index = bisect_left(letters, target)
        if index == len(letters):
            index = 0
        if letters[index] == target:
            index += 1
        if index == len(letters):
            index = 0
        return letters[index]
