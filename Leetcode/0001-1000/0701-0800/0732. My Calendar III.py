# https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree:

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
        self.maxBooked = 0

    def book(self, start: int, end: int) -> int:
        self.update(self.tree, start, end)
        return self.maxBooked

    def update(self, root, start, end):
        if root.isLeaf():
            self.maxBooked = max(self.maxBooked, root.val + 1)
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


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
