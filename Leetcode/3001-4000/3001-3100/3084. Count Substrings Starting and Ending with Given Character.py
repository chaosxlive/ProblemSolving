# leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/


class Solution:

    def countSubstrings(self, s: str, c: str) -> int:
        cnt = s.count(c)
        return (1 + cnt) * cnt // 2
