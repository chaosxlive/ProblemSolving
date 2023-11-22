# https://leetcode.com/problems/count-binary-substrings/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            count0 = count1 = 0
            start0 = end0 = start1 = end1 = False
            for j in range(i, len(s)):
                if s[j] == '0':
                    if end0:
                        break
                    if not start0:
                        start0 = True
                    if start1:
                        end1 = True

                    count0 += 1
                else:
                    if end1:
                        break
                    if not start1:
                        start1 = True
                    if start0:
                        end0 = True

                    count1 += 1

                if count0 == count1:
                    result += 1
        return result
