# https://leetcode.com/problems/distribute-candies-among-children-i/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0

        def cn2(v):
            return v * (v - 1) // 2

        result = cn2(n + 2)

        # Delete case that someone must have candies more than limit
        if n >= limit + 1:
            # result -= 3 * cn2(n + 2 - (limit + 1))
            result -= 3 * cn2(n - limit + 1)
        # Add case that 2 people have candies more than limit
        # if n >= 2 * (limit + 1):
        #     result += 3 * cn2(n + 2 - 2 * (limit + 1))
        if n >= 2 * limit + 2:
            result += 3 * cn2(n - 2 * limit)
        return result
