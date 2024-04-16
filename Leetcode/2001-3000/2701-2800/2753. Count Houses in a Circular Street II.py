# https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a street.
    class Street:

        def closeDoor(self):
            pass

        def isDoorOpen(self):
            pass

        def moveRight(self):
            pass


class Solution:

    def houseCount(self, street: Optional['Street'], k: int) -> int:
        while not street.isDoorOpen():
            street.moveRight()
        result = 0
        for i in range(k):
            street.moveRight()
            if street.isDoorOpen():
                street.closeDoor()
                result = i
        return result + 1
