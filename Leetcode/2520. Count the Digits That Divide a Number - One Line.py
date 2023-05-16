# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution:
    def countDigits(self, num: int) -> int:
        return len(list(filter(lambda n: num % int(n) == 0, str(num))))
