# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestCharCnt = 0
        currentLongestCharCnt = 0
        cnt = defaultdict(int)
        for i in range(len(s)):
            cnt[s[i]] += 1
            currentLongestCharCnt = max(currentLongestCharCnt, cnt[s[i]])
            if longestCharCnt == currentLongestCharCnt + k:
                cnt[s[i - longestCharCnt]] -= 1
            else:
                longestCharCnt += 1
        return longestCharCnt
