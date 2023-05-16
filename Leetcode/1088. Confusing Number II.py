# https://leetcode.com/problems/confusing-number-ii/

class Solution:
    def confusingNumberII(self, n: int) -> int:
        rotateMap = [[0, 0], [1, 1], [6, 9], [8, 8], [9, 6]]
        self.result = 0

        def dfs(num, numRotated, digits):
            if num != numRotated:
                self.result += 1

            for origin, rotated in rotateMap:
                if origin == 0 and num == 0:
                    continue
                if num * 10 + origin > n:
                    break
                dfs(num * 10 + origin, rotated * digits + numRotated, digits * 10)

        dfs(0, 0, 1)
        return self.result
