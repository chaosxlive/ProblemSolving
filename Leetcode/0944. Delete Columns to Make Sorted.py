# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        index = 0
        while index < len(strs[0]):
            prevChar = 'a'
            for s in strs:
                if s[index] < prevChar:
                    result += 1
                    break
                prevChar = s[index]

            index += 1

        return result
