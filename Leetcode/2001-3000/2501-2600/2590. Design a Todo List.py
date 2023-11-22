# https://leetcode.com/problems/design-a-todo-list/

from typing import List
from operator import itemgetter


class TodoList:

    def __init__(self):
        self.unusedIdCounter = 1
        self.userTasks = [[] for _ in range(101)]

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        # [taskId, taskDescription, dueDate, tags, isCompleted]
        self.userTasks[userId].append(
            [self.unusedIdCounter, taskDescription, dueDate, set(tags), False]
        )
        self.unusedIdCounter += 1
        return self.unusedIdCounter - 1

    def getAllTasks(self, userId: int) -> List[str]:
        return list(map(itemgetter(1), sorted(filter(lambda x: not x[4], self.userTasks[userId]), key=itemgetter(2))))

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        return list(map(itemgetter(1), sorted(filter(lambda x: not x[4] and tag in x[3], self.userTasks[userId]), key=itemgetter(2))))

    def completeTask(self, userId: int, taskId: int) -> None:
        for task in self.userTasks[userId]:
            if task[0] == taskId:
                task[4] = True
                break


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)
