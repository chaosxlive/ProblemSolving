# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.first = -1
        self.search(1, n + 1)
        return self.first

    def search(self, left, right):
        if left >= right:
            return

        center = (left + right) // 2

        api_result = isBadVersion(center)
        if api_result and (self.first == -1 or center < self.first):
            self.first = center

        if api_result:
            self.search(left, center)
        else:
            self.search(center + 1, right)
