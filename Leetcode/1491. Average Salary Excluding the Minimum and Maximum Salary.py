# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        maxSalary = minSalary = salary[0]
        total = 0
        for i in range(len(salary)):
            maxSalary = max(maxSalary, salary[i])
            minSalary = min(minSalary, salary[i])
            total += salary[i]
        return (total - maxSalary - minSalary) / (len(salary) - 2)
