# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        rest = k % sum(chalk)
        for index in range(len(chalk)):
            if rest < chalk[index]:
                return index
            rest -= chalk[index]
