# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # https://en.wikipedia.org/wiki/Josephus_problem

        def find(n, k):
            return (find(n - 1, k) + k) % n if n > 1 else 0

        return find(n, k) + 1
