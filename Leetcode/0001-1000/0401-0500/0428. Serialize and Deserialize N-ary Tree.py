# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a Node.
    class Node(object):

        def __init__(self, val=None, children=[]):
            self.val = val
            self.children = children


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: 'Node') -> str:
        if root is None:
            return 'null'
        result = [str(root.val), 'null']
        n = root
        dq = deque()
        while True:
            for c in n.children:
                result.append(str(c.val))
                dq.append(c)
            result.append('null')
            if not dq:
                break
            n = dq.popleft()
        return ','.join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> 'Node':
        if len(data) == 0 or data == 'null':
            return None
        result = Node()
        vs = data.split(',')
        dq = deque()
        n = result
        for v in vs:
            if v == 'null':
                if not dq:
                    break
                n = dq.popleft()
            else:
                nn = Node(int(v))
                dq.append(nn)
                n.children.append(nn)
        return result.children[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
