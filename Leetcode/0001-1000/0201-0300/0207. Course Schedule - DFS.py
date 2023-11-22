# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.paths = [[] for dot in range(numCourses)]
        for path in prerequisites:
            self.paths[path[1]].append(path[0])

        self.visit = [0] * numCourses  # 0: not reached, 1: visited, -1: current passed
        for dot in range(numCourses):
            if not self.dfs(dot):
                return False
        return True

    def dfs(self, index):
        if self.visit[index] == -1:
            return False
        if self.visit[index] == 1:
            return True
        self.visit[index] = -1
        for dot in self.paths[index]:
            if not self.dfs(dot):
                return False
        self.visit[index] = 1
        return True
