# https://leetcode.com/problems/single-threaded-cpu/

from typing import List
import heapq


class Solution:
    def getOrder(self, taskQueue: List[List[int]]) -> List[int]:
        taskQueue = sorted(map(lambda x: [x[1][0], x[1][1], x[0]], enumerate(taskQueue)))  # enqueueTime, processingTime, index
        result = []
        taskQueueIdx = 0
        currentTime = 0
        taskList = []
        while True:
            if len(taskList) == 0:
                if taskQueueIdx < len(taskQueue):
                    currentTime = taskQueue[taskQueueIdx][0]
                    while taskQueueIdx < len(taskQueue) and taskQueue[taskQueueIdx][0] == currentTime:
                        task = taskQueue[taskQueueIdx]
                        taskList.append([task[1], task[2]])  # processingTime, index
                        taskQueueIdx += 1
                    heapq.heapify(taskList)
                else:
                    break
            taskProcessingTime, taskIdx = heapq.heappop(taskList)
            currentTime += taskProcessingTime
            result.append(taskIdx)
            while taskQueueIdx < len(taskQueue) and taskQueue[taskQueueIdx][0] <= currentTime:
                task = taskQueue[taskQueueIdx]
                heapq.heappush(taskList, [task[1], task[2]])  # processingTime, index
                taskQueueIdx += 1
        return result
