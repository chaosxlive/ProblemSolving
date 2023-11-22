# https://leetcode.com/problems/largest-number/

class CmpNumString(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = "".join(sorted(map(str, nums), key=CmpNumString))
        return "0" if result[0] == "0" else result
