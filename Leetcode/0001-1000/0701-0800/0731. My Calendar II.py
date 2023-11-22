# https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:

    class IntervalTreeNode:

        def __init__(self, val=0, start=0, end=2147483647):
            self.start = start
            self.end = end
            self.val = val
            self.left = None
            self.right = None

        def isLeaf(self):
            return self.left == None and self.right == None

    def __init__(self):
        self.tree = self.IntervalTreeNode()

    def book(self, start: int, end: int) -> bool:
        if not self.isAvailable(self.tree, start, end):
            return False

        self.update(self.tree, start, end)

        return True

    def update(self, root, start, end):
        if root.isLeaf():
            if root.start == start and root.end == end:
                root.val += 1
            elif root.start == start:
                root.left = self.IntervalTreeNode(root.val + 1, root.start, end)
                root.right = self.IntervalTreeNode(root.val, end, root.end)
            elif root.end == end:
                root.left = self.IntervalTreeNode(root.val, root.start, start)
                root.right = self.IntervalTreeNode(root.val + 1, start, root.end)
            else:
                root.left = self.IntervalTreeNode(root.val, root.start, end)
                root.left.left = self.IntervalTreeNode(root.val, root.start, start)
                root.left.right = self.IntervalTreeNode(root.val + 1, start, end)
                root.right = self.IntervalTreeNode(root.val, end, root.end)
        else:
            if root.left.end <= start:
                self.update(root.right, start, end)
            elif end <= root.right.start:
                self.update(root.left, start, end)
            else:
                self.update(root.left, start, root.left.end)
                self.update(root.right, root.right.start, end)

    def isAvailable(self, root, start, end):
        if root.isLeaf() and root.start <= start and end <= root.end:
            return root.val < 2
        if root.left.end > start and not self.isAvailable(root.left, start, min(root.left.end, end)):
            return False
        if root.right.start < end and not self.isAvailable(root.right, max(root.right.start, start), end):
            return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
