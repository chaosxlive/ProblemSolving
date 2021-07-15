# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        counts = [1] * 5

        def nextPermutation(counts):
            result = [0] * 5
            result[0] = counts[1] + counts[2] + counts[4]
            result[1] = counts[0] + counts[2]
            result[2] = counts[1] + counts[3]
            result[3] = counts[2]
            result[4] = counts[2] + counts[3]
            for i in range(5):
                counts[i] = result[i] % 1000000007

        for i in range(2, n + 1):
            nextPermutation(counts)

        return sum(counts) % 1000000007
