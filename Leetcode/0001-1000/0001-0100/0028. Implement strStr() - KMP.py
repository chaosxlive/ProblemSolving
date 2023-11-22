# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0

        next = [-1 for i in range(len(needle) + 1)]
        k = 0
        for l in range(1, len(needle)):
            k = next[l - 1]
            while k >= 0 and needle[k + 1] != needle[l]:
                k = next[k]
            if needle[k + 1] == needle[l]:
                next[l] = k + 1

        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = next[j - 1] + 1
            else:
                i += 1
        return i - len(needle) if j == len(needle) else -1
