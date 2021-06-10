# https://leetcode.com/problems/find-the-shortest-superstring/

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        lengthWords = len(words)
        cost = [[0 for col in range(lengthWords)] for row in range(lengthWords)]
        for i in range(lengthWords):
            for j in range(lengthWords):
                cost[i][j] = len(words[j])
                for k in range(1, min(len(words[i]), len(words[j])) + 1):
                    if words[i][-k:] == words[j][:k]:
                        cost[i][j] = len(words[j]) - k
        for i in range(lengthWords):
            cost[i][i] = len(words[i])

        dp = [[2147483647 for j in range(lengthWords)] for i in range(1 << lengthWords)]
        parent = [[-1 for j in range(lengthWords)] for i in range(1 << lengthWords)]

        for i in range(lengthWords):
            dp[1 << i][i] = len(words[i])

        for s in range(1, 1 << lengthWords):
            for i in range(lengthWords):
                if (s & 1 << i) == 0:
                    continue
                prev = s - (1 << i)
                for j in range(lengthWords):
                    if dp[prev][j] + cost[j][i] < dp[s][i]:
                        dp[s][i] = dp[prev][j] + cost[j][i]
                        parent[s][i] = j

        ptr = dp[-1].index(min(dp[-1]))
        s = (1 << lengthWords) - 1
        result = []
        while s != 0:
            prev = parent[s][ptr]
            if prev < 0:
                result = [words[ptr]] + result
            else:
                result = [words[ptr][-cost[prev][ptr]:]] + result
            s &= ~(1 << ptr)
            ptr = prev

        return "".join(result)
