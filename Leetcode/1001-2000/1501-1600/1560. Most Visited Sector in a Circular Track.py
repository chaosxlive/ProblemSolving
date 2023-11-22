# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        return list(range(rounds[0], rounds[-1] + 1)) if rounds[-1] >= rounds[0] else (list(range(1, rounds[-1] + 1)) + list(range(rounds[0], n + 1)))
