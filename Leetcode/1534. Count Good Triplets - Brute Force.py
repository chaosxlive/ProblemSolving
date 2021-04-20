# https://leetcode.com/problems/count-good-triplets/

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        result = 0
        for index1 in range(length - 2):
            for index2 in range(index1 + 1, length - 1):
                for index3 in range(index2 + 1, length):
                    if abs(arr[index1] - arr[index2]) <= a and abs(arr[index2] - arr[index3]) <= b and abs(arr[index1] - arr[index3]) <= c:
                        result += 1
        return result
