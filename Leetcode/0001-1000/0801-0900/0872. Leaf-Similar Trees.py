# https://leetcode.com/problems/leaf-similar-trees/

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def findLeaf(leaves, root):
            if root == None:
                return
            if root.left == None and root.right == None:
                leaves.append(root.val)
            if root.left != None:
                findLeaf(leaves, root.left)
            if root.right != None:
                findLeaf(leaves, root.right)

        leaves1, leaves2 = [], []

        findLeaf(leaves1, root1)
        findLeaf(leaves2, root2)

        return tuple(leaves1) == tuple(leaves2)
