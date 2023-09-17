# https://leetcode.com/problems/count-symmetric-integers/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            l = len(str(i))
            if l % 2 == 0:
                n = i
                s = e = 0
                for i in range(l // 2):
                    s += n % 10
                    n //= 10
                for i in range(l // 2):
                    e += n % 10
                    n //= 10
                if s == e:
                    count += 1
        return count
