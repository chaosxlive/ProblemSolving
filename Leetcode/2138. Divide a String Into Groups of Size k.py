# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        last = 0
        while last < len(s):
            temp = s[last:last + k]
            if len(temp) < k:
                temp = temp + fill * (k - len(temp))
            result.append(temp)
            last += k
        return result
