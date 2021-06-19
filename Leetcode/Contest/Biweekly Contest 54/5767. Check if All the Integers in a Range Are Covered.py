# https://leetcode.com/contest/biweekly-contest-54/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            isInclude = False
            for inteval in ranges:
                if inteval[0] <= num <= inteval[1]:
                    isInclude = True
                    break
            if not isInclude:
                return False
        return True
