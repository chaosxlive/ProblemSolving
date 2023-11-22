# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def dfs(n, k, s, used, current, result):
            if len(current) == k:
                result.append(current[:])
            for i in range(s, n + 1):
                if not used[i]:
                    used[i] = True
                    current.append(i)
                    dfs(n, k, i + 1, used, current, result)
                    current.pop()
                    used[i] = False

        dfs(n, k, 1, [False] * (n + 1), [], result)
        return result
