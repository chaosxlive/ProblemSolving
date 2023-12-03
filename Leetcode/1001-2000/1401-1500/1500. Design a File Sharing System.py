# https://leetcode.com/problems/design-a-file-sharing-system/

import heapq
from typing import List


class FileSharing:

    def __init__(self, m: int):
        self.owners = [set() for _ in range(m + 1)]
        self.usableIds = []
        self.lastId = 1

    def join(self, ownedChunks: List[int]) -> int:
        if len(self.usableIds) == 0:
            userId = self.lastId
            self.lastId += 1
        else:
            userId = heapq.heappop(self.usableIds)
        for chunkId in ownedChunks:
            self.owners[chunkId].add(userId)
        return userId

    def leave(self, userID: int) -> None:
        for o in self.owners:
            if userID in o:
                o.remove(userID)
        heapq.heappush(self.usableIds, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        ret = sorted(self.owners[chunkID])
        if len(ret) > 0:
            self.owners[chunkID].add(userID)
        return ret


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)
