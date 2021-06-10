# https://leetcode.com/contest/weekly-contest-243/problems/maximum-value-after-insertion/

import heapq


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        heap = []
        for index in range(len(servers)):
            heapq.heappush(heap, [servers[index], index])

        running = []
        time = 0
        index = 0
        result = []
        while True:
            while len(running) != 0 and running[0][0] <= time:
                heapq.heappush(heap, heapq.heappop(running)[1])
            if len(heap) == 0:
                time = running[0][0]
                continue
            while len(heap) != 0 and time >= index:
                server = heapq.heappop(heap)
                result.append(server[1])
                heapq.heappush(running, [time + tasks[index], server])
                index += 1
                if index == len(tasks):
                    return result
            time += 1
