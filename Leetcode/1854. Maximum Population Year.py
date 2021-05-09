# https://leetcode.com/problems/maximum-population-year/

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        maxCount = maxYear = 0
        for year in range(1950, 2051):
            count = 0
            for log in logs:
                if log[0] <= year < log[1]:
                    count += 1
            if count > maxCount:
                maxCount = count
                maxYear = year

        return maxYear
