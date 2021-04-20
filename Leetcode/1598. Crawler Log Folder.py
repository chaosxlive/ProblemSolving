# https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for cmd in logs:
            if cmd == '../' and depth != 0:
                depth -= 1
            elif cmd == './' or (cmd == '../' and depth == 0):
                pass
            else:
                depth += 1
        return depth