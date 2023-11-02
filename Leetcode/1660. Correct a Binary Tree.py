# https://leetcode.com/problems/correct-a-binary-tree/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = set()

        def dfs(parent: Optional[TreeNode], isRight: bool, node: TreeNode):
            seen.add(node)
            if node.right is not None:
                if node.right in seen:
                    if isRight:
                        parent.right = None
                        return True
                    else:
                        parent.left = None
                        return True
                if dfs(node, True, node.right):
                    return True
            if node.left is not None:
                if dfs(node, False, node.left):
                    return True
            return False

        dfs(None, False, root)
        return root
