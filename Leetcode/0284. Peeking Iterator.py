# https://leetcode.com/problems/peeking-iterator/

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nextElement = 0
        self.iterator = iterator
        self.isPeeked = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.isPeeked:
            self.nextElement = self.iterator.next()
            self.isPeeked = True
        return self.nextElement

    def next(self):
        """
        :rtype: int
        """
        if self.isPeeked:
            self.isPeeked = False
            return self.nextElement
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.isPeeked:
            return True
        return self.iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
