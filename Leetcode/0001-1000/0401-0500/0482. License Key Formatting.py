# https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        fullStr = "".join(s.split('-'))
        if len(fullStr) % k == 0:
            result = []
        else:
            result = [fullStr[:len(fullStr) % k]]
        for i in range(len(fullStr) // k):
            result.append(fullStr[i * k + len(fullStr) % k: i * k + len(fullStr) % k + k])
        return "-".join(result).upper()
