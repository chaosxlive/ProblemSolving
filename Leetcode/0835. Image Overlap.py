# https://leetcode.com/problems/image-overlap/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        length = len(img1)
        digits1 = [int(''.join(map(lambda x: str(x), row)), 2) for row in img1]
        digits2 = [int(''.join(map(lambda x: str(x), row)), 2) for row in img2]

        def countBits(a, b):
            temp = 0
            for i in range(length):
                num = a[i] & b[i]
                for _bit in range(length):
                    temp += num & 1
                    num >>= 1
            return temp

        result = 0
        for h in range(length):
            leftDigits1 = [0] * length + list(map(lambda x: x << h, digits1)) + [0] * length
            for v in range(2 * length):
                finalDigits = leftDigits1[v:v + length]
                result = max(result, countBits(finalDigits, digits2))
        for h in range(length):
            leftDigits1 = [0] * length + list(map(lambda x: x >> h, digits1)) + [0] * length
            for v in range(2 * length):
                finalDigits = leftDigits1[v:v + length]
                result = max(result, countBits(finalDigits, digits2))
        return result

# Possibly TLE, but it works sometimes.