# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        seen = [0] * 100001

        def dfs(seen, root):
            if not root:
                return

            seen[root.val] += 1

            dfs(seen, root.left)
            dfs(seen, root.right)

        dfs(seen, root)

        prev = -1
        result = 100001
        for i in range(100001):
            if seen[i]:
                if prev != -1:
                    if seen[i] >= 2:
                        return 0

                    result = min(result, i - prev)
                prev = i

        return result
