# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = 0
        for candy in candies:
            if candy > maxCandy:
                maxCandy = candy

        result = []
        threshold = maxCandy - extraCandies
        for candy in candies:
            result.append(candy >= threshold)

        return result
                