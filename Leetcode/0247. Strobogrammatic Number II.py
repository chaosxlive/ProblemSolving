# https://leetcode.com/problems/strobogrammatic-number-ii/

class Solution:
    def findStrobogrammatic(self, n: int, isFirst=True) -> List[str]:
        if n == 1:
            return ["0", "1", "8"]
        if n == 2:
            if isFirst:
                return ["11", "69", "88", "96"]
            else:
                return ["00", "11", "69", "88", "96"]
        candidates = self.findStrobogrammatic(n - 2, isFirst=False)
        result = []
        for candidate in candidates:
            digits = [("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
            if not isFirst:
                digits.append(("0", "0"))
            for pair in digits:
                result.append(pair[0] + candidate + pair[1])
        return result
