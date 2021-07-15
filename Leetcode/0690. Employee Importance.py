# https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        relates = {}
        for employee in employees:
            relates[employee.id] = employee

        def traversal(relates, id):
            importance = 0
            for subordinate in relates[id].subordinates:
                importance += traversal(relates, subordinate)
            return importance + relates[id].importance

        return traversal(relates, id)
