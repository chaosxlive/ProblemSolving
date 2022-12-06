# https://leetcode.com/problems/design-a-leaderboard/

class Leaderboard:

    def __init__(self):
        self.container = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.container:
            self.container[playerId] = score
        else:
            self.container[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.container.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        self.container.pop(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
