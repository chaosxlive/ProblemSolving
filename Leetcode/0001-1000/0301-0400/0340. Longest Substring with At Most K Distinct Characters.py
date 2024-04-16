# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

from collections import defaultdict


class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        left, right = 0, 0
        counter = defaultdict(int)
        unique = 0
        result = 0
        while right < len(s):
            if counter[s[right]] == 0:
                unique += 1
            counter[s[right]] += 1
            while unique > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    unique -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return max(result, right - left)
