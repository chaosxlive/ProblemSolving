# https://leetcode.com/problems/longest-absolute-file-path/

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        pathes = input.split('\n')
        lengthStack = [0]
        idx = 0
        result = 0
        while idx < len(pathes):
            path = pathes[idx]
            isFile = path.find('.') > -1
            level = path.count('\t')
            while len(lengthStack) > 1 and len(lengthStack) - 1 > level:
                lengthStack.pop()
            lengthStack.append(lengthStack[-1] + len(path[level:]))
            if isFile:
                result = max(result, lengthStack[-1] + len(lengthStack) - 2)
                lengthStack.pop()
            idx += 1
        return result
