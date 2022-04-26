# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        if k == 0:
            return num

        s = []
        s.append(num[0])

        for i in range(1, len(num)):
            while k > 0 and len(s) > 0 and num[i] < s[-1]:
                s.pop()
                k -= 1
            s.append(num[i])

            if len(s) == 1 and num[i] == '0':
                s.pop()

        while k > 0 and len(s) > 0:
            s.pop()
            k -= 1

        result = []
        while len(s) > 0:
            result += s.pop()

        if len(result) == 0:
            return '0'

        return ''.join(result[::-1])
