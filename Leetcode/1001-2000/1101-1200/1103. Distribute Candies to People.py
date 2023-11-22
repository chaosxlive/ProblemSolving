# https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        index = 0
        while candies > 0:
            given = min(candies, index + 1)
            result[index % num_people] += given
            candies -= given
            index += 1
        return result
