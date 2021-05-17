# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curSum = countOdd = 0
        for num in arr:
            curSum += num
            if curSum % 2 == 1:
                countOdd += 1

        return countOdd * (len(arr) - countOdd + 1) % (10 ** 9 + 7)
