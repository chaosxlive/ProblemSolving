# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        index = 0
        result = []
        for i in range(1, n + 1):
            if i == target[index]:
                result.append("Push")
                index += 1
                if index == len(target):
                    return result
            else:
                result.append("Push")
                result.append("Pop")
        return result
