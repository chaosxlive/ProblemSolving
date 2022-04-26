# https://leetcode.com/problems/find-mode-in-binary-search-tree/

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, counter):
            if not root:
                return
            counter[root.val] += 1
            dfs(root.left, counter)
            dfs(root.right, counter)

        counter = defaultdict(int)
        dfs(root, counter)
        max_count = max(counter.values())
        return [k for k, v in counter.items() if v == max_count]
