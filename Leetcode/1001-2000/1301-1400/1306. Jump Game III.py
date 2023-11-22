# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.arr = arr
        self.visited = [False] * len(arr)
        return self.dfs(start)

    def dfs(self, current):
        if self.arr[current] == 0:
            return True
        left = current - self.arr[current]
        if left >= 0 and not self.visited[left]:
            self.visited[left] = True
            if self.dfs(left):
                return True
        right = current + self.arr[current]
        if right < len(self.arr) and not self.visited[right]:
            self.visited[right] = True
            if self.dfs(right):
                return True
        return False
