# https://leetcode.com/problems/largest-number-after-mutating-substring/

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        chars = [int(c) for c in num]
        isChanged = False
        for i in range(len(chars)):
            if isChanged and change[chars[i]] < chars[i]:
                break
            else:
                if change[chars[i]] > chars[i]:
                    isChanged = True
                    chars[i] = change[chars[i]]
        return "".join([str(n) for n in chars])
