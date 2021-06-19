# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        nums = self.countAndSay(n - 1)
        count = 1
        prev = nums[0]
        result = []
        for i in range(1, len(nums)):
            if nums[i] == prev:
                count += 1
            else:
                result.append(str(count))
                result.append(prev)
                prev = nums[i]
                count = 1
        result.append(str(count))
        result.append(prev)
        return "".join(result)
