# https://leetcode.com/problems/count-houses-in-a-circular-street/

from typing import Optional


# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        for i in range(k):
            street.closeDoor()
            street.moveRight()
        result = 0
        while not street.isDoorOpen():
            street.openDoor()
            result += 1
            street.moveRight()
        return result
