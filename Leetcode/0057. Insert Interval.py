# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        index = 0
        while index < len(intervals) and newInterval[0] > intervals[index][1]:
            result.append([intervals[index][0], intervals[index][1]])
            index += 1
        if index == len(intervals):
            result.append(newInterval)
            return result
        if newInterval[1] < intervals[index][0]:
            result.append(newInterval)
            while index < len(intervals):
                result.append([intervals[index][0], intervals[index][1]])
                index += 1
            return result
        left = min(intervals[index][0], newInterval[0])
        while index < len(intervals) and newInterval[1] >= intervals[index][0]:
            right = max(intervals[index][1], newInterval[1])
            index += 1
        result.append([left, right])
        while index < len(intervals):
            result.append([intervals[index][0], intervals[index][1]])
            index += 1
        return result
