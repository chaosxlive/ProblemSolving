from collections import deque


class SegmentTreeNode:

    def __init__(self, v=0, boundLeft=-float('inf'), boundRight=float('inf'), left=None, right=None) -> None:
        self.v = v
        self.dirty = 0
        self.boundLeft = boundLeft
        self.boundRight = boundRight
        self.left = left
        self.right = right


class SegmentTree:

    def __init__(self, left=0, right=0, data=[0]) -> None:
        self.root = SegmentTreeNode(boundLeft=left, boundRight=right)

        def build(n):
            if n.boundLeft != n.boundRight:
                mid = n.boundLeft + (n.boundRight - n.boundLeft) // 2
                n.left = SegmentTreeNode(boundLeft=n.boundLeft, boundRight=mid)
                n.right = SegmentTreeNode(boundLeft=mid + 1, boundRight=n.boundRight)
                n.v = max(n.v, build(n.left))
                n.v = max(n.v, build(n.right))
            else:
                n.v = data[n.boundLeft]
            return n.v

        build(self.root)

    def update(self, left, right, v):

        def dfs(n, newD, oldD):
            l = n.boundLeft
            r = n.boundRight
            if right < l or left > r:
                n.dirty += oldD
                return n.v + n.dirty
            if left <= l and r <= right:
                n.dirty += newD + oldD
            else:
                n.v = max(n.v, dfs(n.left, newD, n.dirty))
                n.v = max(n.v, dfs(n.right, newD, n.dirty))
                n.dirty = 0
            return n.v + n.dirty

        dfs(self.root, v, 0)

    def range(self, left, right):
        result = [0] * (right - left + 1)

        def dfs(n, d):
            l = n.boundLeft
            r = n.boundRight
            if right < l or left > r:
                n.dirty += d
                return n.v + n.dirty
            if l == r:
                n.v += n.dirty
                result[l - left] = n.v
            else:
                n.v = max(n.v, dfs(n.left, n.dirty + d))
                n.v = max(n.v, dfs(n.right, n.dirty + d))
            n.dirty = 0
            return n.v
        
        dfs(self.root, 0)
        return result

    def get(self, i):
        return self.range(i, i)[0]



a = SegmentTree(0, 10, [0] * 11)
a.update(2, 5, 3)
print(a.range(0, 10))
a.update(1, 3, 1)
print(a.get(5))
print(a.get(3))
print(a.get(7))
print(a.get(5))
print(a.range(0, 10))
print(a.get(5))
print(a.get(2))
pass
