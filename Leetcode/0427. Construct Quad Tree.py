# https://leetcode.com/problems/construct-quad-tree/

from typing import List


# Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid

        def build(l: int, r: int, t: int, b: int) -> 'Node':
            if r - l == 1 and b - t == 1:
                return Node(self.grid[t][l], True, None, None, None, None)
            tl = build(l, l + (r - l) // 2, t, t + (b - t) // 2)
            tr = build(l + (r - l) // 2, r, t, t + (b - t) // 2)
            bl = build(l, l + (r - l) // 2, t + (b - t) // 2, b)
            br = build(l + (r - l) // 2, r, t + (b - t) // 2, b)
            if tl.isLeaf and bl.isLeaf and tr.isLeaf and br.isLeaf and tl.val == bl.val == tr.val == br.val:
                return tl
            else:
                return Node(0, False, tl, tr, bl, br)

        return build(0, len(grid[0]), 0, len(grid))
