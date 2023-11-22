# https://leetcode.com/problems/remove-boxes/

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @cache
        def dp(left, right, count):
            if left > right:
                return 0
            while left + 1 <= right and boxes[left] == boxes[left + 1]:
                left += 1
                count += 1
            result = (count + 1) * (count + 1) + dp(left + 1, right, 0)
            for index in range(left + 1, right + 1):
                if boxes[left] == boxes[index]:
                    result = max(result, dp(left + 1, index - 1, 0) + dp(index, right, count + 1))
            return result

        return dp(0, len(boxes) - 1, 0)
