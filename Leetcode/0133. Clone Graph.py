# https://leetcode.com/problems/clone-graph/

from collections import deque

# Definition for a Node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        oldToNew = {}
        oldToNew[id(None)] = None
        oldToNew[id(node)] = Node(node.val)
        q = deque()
        q.append(node)
        visited = set()
        while len(q) > 0:
            oldNode = q.popleft()
            visited.add(id(oldNode))
            clonedNode = oldToNew[id(oldNode)]
            for oldNeighbor in oldNode.neighbors:
                if id(oldNeighbor) in visited:
                    continue
                if id(oldNeighbor) not in oldToNew:
                    oldToNew[id(oldNeighbor)] = Node(oldNeighbor.val)
                neighborNode = oldToNew[id(oldNeighbor)]
                clonedNode.neighbors.append(neighborNode)
                neighborNode.neighbors.append(clonedNode)
                q.append(oldNeighbor)
        return oldToNew[id(node)]
