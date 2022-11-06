# https://leetcode.com/problems/word-break-ii/

from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = defaultdict(lambda: [])
        for word in wordDict:
            words[word[0]].append(word)

        dp = defaultdict(lambda: [])
        dp[0].append(('',))

        for i in range(len(s)):
            if len(dp[i]) > 0:
                for word in words[s[i]]:
                    if word == s[i:i + len(word)]:
                        for possible in dp[i]:
                            dp[i + len(word)].append(possible + (word,))
        return list(map(lambda x: ' '.join(x[1:]), dp[len(s)]))
