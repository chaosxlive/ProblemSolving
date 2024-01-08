# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

class Solution:
    def maximumLength(self, s: str) -> int:
        cnts = [[] for i in range(26)]
        prev = 0
        i = 1
        while i < len(s):
            if s[i] != s[prev]:
                cnts[ord(s[prev])-ord('a')].append(i - prev)
                prev = i
            i += 1
        cnts[ord(s[prev])-ord('a')].append(i - prev)
        result = -1
        for cnt in cnts:
            cnt.sort(reverse=True)
            if len(cnt) >= 3:
                result = max(result, cnt[2], min(cnt[0] - 1, cnt[1]), cnt[0] - 2)
            elif len(cnt) == 2:
                result = max(result, min(cnt[0] - 1, cnt[1]), cnt[0] - 2)
            if len(cnt) >= 1:
                result = max(result, cnt[0] - 2)
        return result if result > 0 else -1
