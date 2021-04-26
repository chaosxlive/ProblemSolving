# https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        self.result = 0
        self.heights = heights

        self.dfs(0, bricks, ladders)

        return self.result

    
    def dfs(self, index, bricks, ladders):
        if index > self.result:
            self.result = index
        
        if index == len(self.heights) - 1:
            return
        
        if self.heights[index] < self.heights[index + 1]:
            if ladders > 0:
                self.dfs(index + 1, bricks, ladders - 1)
            
            difHeight = self.heights[index + 1] - self.heights[index]
            if bricks >= difHeight:
                self.dfs(index + 1, bricks - difHeight, ladders)
        else:
            self.dfs(index + 1, bricks, ladders)
