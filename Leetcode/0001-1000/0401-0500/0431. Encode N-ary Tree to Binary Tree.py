# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a Node.
    class Node:

        def __init__(self, val: int = None, children: 'List[Node]' = None):
            self.val = val
            self.children = children

    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, x: int):
            self.val = x
            self.left = None
            self.right = None


class Codec:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> 'Optional[TreeNode]':
        if root is None:
            return None
        result = TreeNode(root.val)
        ns = list(reversed(root.children))
        if len(ns) == 0:
            return result
        result.right = TreeNode(len(ns))
        ptr = result.right
        while len(ns) > 2:
            ptr.right = self.encode(ns.pop())
            ptr.left = TreeNode()
            ptr = ptr.left
        if len(ns) == 2:
            ptr.right = self.encode(ns.pop())
            ptr.left = self.encode(ns.pop())
        elif len(ns) == 1:
            ptr.right = self.encode(ns.pop())
        return result

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: 'Optional[TreeNode]') -> 'Optional[Node]':
        if data is None:
            return None
        result = Node(data.val, [])
        if data.right is None:
            return result
        cnt = data.right.val
        ptr = data.right
        while cnt > 2:
            result.children.append(self.decode(ptr.right))
            ptr = ptr.left
            cnt -= 1
        if cnt == 2:
            result.children.append(self.decode(ptr.right))
            result.children.append(self.decode(ptr.left))
        elif cnt == 1:
            result.children.append(self.decode(ptr.right))
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
