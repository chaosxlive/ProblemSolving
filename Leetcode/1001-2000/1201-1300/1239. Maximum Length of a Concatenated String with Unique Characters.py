# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for s in arr:
            tempMask = 0
            isValid = True
            for c in s:
                bit = 1 << ord(c) - ord('a')
                if tempMask & bit > 0:
                    isValid = False
                    break
                tempMask |= bit
            if isValid:
                masks.append((tempMask, len(s)))

        def force(index, picked, current, count):
            if index >= len(masks):
                return count
            result = count
            if picked:
                if current & masks[index][0] > 0:
                    return 0
                result = max(result, force(index + 1, True, current | masks[index][0], count + masks[index][1]))
                result = max(result, force(index + 1, False, current | masks[index][0], count + masks[index][1]))
            else:
                result = max(result, force(index + 1, True, current, count))
                result = max(result, force(index + 1, False, current, count))
            return result

        return force(-1, False, 0, 0)