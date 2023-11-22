# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path = []
        result = []

        def traverse(result, path, root):
            path.append(str(root.val))
            if root.left == None and root.right == None:
                result.append("".join(path))
                path.pop()
                return
            path.append("->")
            if root.left != None:
                traverse(result, path, root.left)
            if root.right != None:
                traverse(result, path, root.right)
            path.pop()
            path.pop()

        traverse(result, path, root)
        return result
