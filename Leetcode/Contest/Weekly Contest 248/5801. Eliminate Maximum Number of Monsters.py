# https://leetcode.com/contest/weekly-contest-248/problems/eliminate-maximum-number-of-monsters/

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsters = []
        for i in range(len(dist)):
            monsters.append(((dist[i] - 1) // speed[i], dist, speed))
        monsters.sort()

        result = 0
        for time in range(len(dist)):
            if time <= monsters[time][0]:
                result += 1
            else:
                return result
        return result
