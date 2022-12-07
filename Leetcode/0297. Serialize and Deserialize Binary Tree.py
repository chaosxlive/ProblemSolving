# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from collections import deque
import json


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return json.dumps([])
        result = []
        q = deque([root])
        while q:
            n = q.popleft()
            if n is None:
                result.append(None)
            else:
                result.append(n.val)
                q.append(n.left)
                q.append(n.right)
        return json.dumps(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = json.loads(data)
        if len(arr) == 0:
            return None
        result = TreeNode(arr[0])
        q = deque([result])
        idx = 1
        while idx < len(arr):
            n = q.popleft()
            left = arr[idx]
            if left is None:
                n.left = None
            else:
                n.left = TreeNode(left)
                q.append(n.left)
            idx += 1
            right = arr[idx]
            if right is None:
                n.right = None
            else:
                n.right = TreeNode(right)
                q.append(n.right)
            idx += 1
        return result


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
