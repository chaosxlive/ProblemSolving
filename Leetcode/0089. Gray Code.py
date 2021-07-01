# https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        mask = 1
        for i in range(1, n + 1):
            length = len(result)
            for index in range(length - 1, -1, -1):
                result.append(result[index] + mask)
            mask <<= 1
        return result
