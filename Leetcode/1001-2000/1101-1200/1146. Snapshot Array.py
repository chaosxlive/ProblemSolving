# https://leetcode.com/problems/snapshot-array/

import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.container = [[[0, 0]] for i in range(length)]
        self.currentId = 0

    def set(self, index: int, val: int) -> None:
        if self.container[index][-1][0] != self.currentId:
            self.container[index].append([self.currentId, val])
        else:
            self.container[index][-1][1] = val

    def snap(self) -> int:
        self.currentId += 1
        return self.currentId - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.container[index][bisect.bisect_left(self.container[index], [snap_id, 2147483647]) - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
