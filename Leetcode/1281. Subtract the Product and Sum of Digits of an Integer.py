# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        sum_num = 0
        product = 1

        while n > 0:
            sum_num += n % 10
            product *= n % 10
            n //= 10
        
        return product - sum_num