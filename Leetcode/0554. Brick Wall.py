# https://leetcode.com/problems/brick-wall/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {0: 0}
        for row in wall:
            sum = 0
            for brick in row[:-1]:
                sum += brick
                if sum in edges:
                    edges[sum] += 1
                else:
                    edges[sum] = 1

        return len(wall) - max(edges.values())
