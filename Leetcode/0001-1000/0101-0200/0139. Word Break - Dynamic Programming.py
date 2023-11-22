# https://leetcode.com/problems/word-break/

from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = defaultdict(lambda: [])
        for word in wordDict:
            words[word[0]].append(word)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i]:
                for word in words[s[i]]:
                    if word == s[i:i + len(word)]:
                        dp[i + len(word)] = True
        return dp[-1]
