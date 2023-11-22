# https://leetcode.com/problems/keys-and-rooms/

from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        canVisit = set([0])
        q = deque([0])

        while len(q) > 0:
            roomId = q.popleft()
            for key in rooms[roomId]:
                if key not in canVisit:
                    canVisit.add(key)
                    q.append(key)

        return len(canVisit) == len(rooms)
