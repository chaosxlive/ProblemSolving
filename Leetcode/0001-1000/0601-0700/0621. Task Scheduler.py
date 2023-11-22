# https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = {}
        for task in tasks:
            if task not in frequency:
                frequency[task] = 1
            else:
                frequency[task] += 1
        frequency = sorted(list(map(lambda x: [x[0], x[1]], frequency.items())), key=lambda x: x[1], reverse=True)

        index = 1
        while index < len(frequency):
            if frequency[index][1] < frequency[index - 1][1]:
                break
            index += 1
        countEnough = index * frequency[0][1]
        countNotEnough = (n + 1) * (frequency[0][1] - 1) + index
        if countEnough > countNotEnough:
            return len(tasks)
        else:
            return max(countNotEnough - countEnough, len(tasks) - frequency[0][1] * index) + index * frequency[0][1]

# Reference:
# https://leetcode.com/problems/task-scheduler/discuss/761070/Python-or-Heavily-visualized-%2B-Detailed-explanation