# https://leetcode.com/problems/find-duplicate-subtrees/

from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.result = []
        self.idMap = {}
        self.idCnt = 1

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val not in self.idMap:
                self.idMap[root.val] = self.idCnt
                self.idCnt += 1
            cur = self.idMap[root.val]
            result = (left, cur, right)
            if result in self.idMap:
                if not self.idMap[result][0]:
                    self.result.append(root)
                    self.idMap[result][0] = True
            else:
                self.idMap[result] = [False, self.idCnt]
                self.idCnt += 1
            return self.idMap[result][1]

        dfs(root)
        return self.result
