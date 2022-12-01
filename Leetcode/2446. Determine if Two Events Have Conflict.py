# https://leetcode.com/problems/determine-if-two-events-have-conflict/

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        def isOverlapped(s1, e1, s2, e2):
            return s1 <= e2 and s2 <= e1

        return isOverlapped(event1[0], event1[1], event2[0], event2[1])
