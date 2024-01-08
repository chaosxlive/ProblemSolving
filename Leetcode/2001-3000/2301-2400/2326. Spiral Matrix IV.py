# https://leetcode.com/problems/spiral-matrix-iv/

from typing import TYPE_CHECKING, Optional, List


if TYPE_CHECKING:

    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ptr = head
        di = 0
        pr = pc = 0
        result = [[-1] * n for _ in range(m)]

        while ptr is not None:
            result[pr][pc] = ptr.val
            ptr = ptr.next
            while ptr is not None:
                dr, dc = dirs[di]
                if not (0 <= pr + dr < m and 0 <= pc + dc < n) or result[pr + dr][pc + dc] != -1:
                    di = (di + 1) % 4
                    continue
                pr += dr
                pc += dc
                break
        return result
