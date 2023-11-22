# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCount = [0] * (n + 1)
        trustedCount = [0] * (n + 1)
        for t in trust:
            trustCount[t[0]] += 1
            trustedCount[t[1]] += 1
        for i in range(1, n + 1):
            if trustCount[i] == 0 and trustedCount[i] == n - 1:
                return i
        return -1
