# https://leetcode.com/problems/find-unique-binary-string/

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join(['0' if num[i] == '1' else '1' for i, num in enumerate(nums)])
