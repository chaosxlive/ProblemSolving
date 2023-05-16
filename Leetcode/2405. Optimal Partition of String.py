# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    seen = [False] * 26

    def partitionString(self, s: str) -> int:
        self.reset()
        result = 1
        for c in s:
            if self.seen[ord(c) - 97]:
                self.reset()
                result += 1
            self.seen[ord(c) - 97] = True
        return result

    def reset(self):
        self.seen = [False] * 26
