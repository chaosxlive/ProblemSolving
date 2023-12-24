# https://leetcode.com/problems/unique-binary-search-trees-ii/

from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def genTrees(candidates: List[int]) -> List[TreeNode]:
            result = []
            for i, v in enumerate(candidates):
                lefts = genTrees(candidates[:i])
                rights = genTrees(candidates[i + 1:])
                if len(lefts) == 0:
                    lefts.append(None)
                if len(rights) == 0:
                    rights.append(None)
                for left in lefts:
                    for right in rights:
                        result.append(TreeNode(v, left, right))
            return result

        return genTrees(list(i for i in range(1, n + 1)))
