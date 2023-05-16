# https://leetcode.com/problems/handling-sum-queries-after-update/

from typing import List
import math


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        self.nums1 = nums1
        self.nums2 = nums2
        self.blockSize = math.isqrt(len(nums1))
        self.isBlockDirty = [False] * (len(nums1) // self.blockSize + 1)
        self.blockCount = [sum(self.nums1[j] for j in range(i * self.blockSize, min(len(nums1), (i + 1) * self.blockSize))) for i in range(len(self.isBlockDirty))]
        self.count = sum(self.blockCount)
        self.result = sum(nums2)

        def op1(L, R):
            blockL = L // self.blockSize
            blockR = R // self.blockSize

            if self.isBlockDirty[blockL]:
                self.count -= self.blockCount[blockL]
                self.blockCount[blockL] = self.blockSize - self.blockCount[blockL]
                self.count += self.blockCount[blockL]
                for i in range(blockL * self.blockSize, L):
                    if nums1[i] == 0:
                        nums1[i] = 1
                        self.blockCount[blockL] += 1
                        self.count += 1
                    else:
                        nums1[i] = 0
                        self.blockCount[blockL] -= 1
                        self.count -= 1
                for i in range(R + 1, (blockL + 1) * self.blockSize):
                    if nums1[i] == 0:
                        nums1[i] = 1
                        self.blockCount[blockL] += 1
                        self.count += 1
                    else:
                        nums1[i] = 0
                        self.blockCount[blockL] -= 1
                        self.count -= 1
            else:
                for i in range(L, min(R + 1, (blockL + 1) * self.blockSize)):
                    if nums1[i] == 0:
                        nums1[i] = 1
                        self.blockCount[blockL] += 1
                        self.count += 1
                    else:
                        nums1[i] = 0
                        self.blockCount[blockL] -= 1
                        self.count -= 1
            self.isBlockDirty[blockL] = False
            if blockL == blockR:
                return
            for i in range(blockL + 1, blockR):
                self.isBlockDirty[i] = not self.isBlockDirty[i]
                self.count -= self.blockCount[i]
                self.blockCount[i] = self.blockSize - self.blockCount[i]
                self.count += self.blockCount[i]
            if self.isBlockDirty[blockR]:
                self.count -= self.blockCount[blockR]
                self.blockCount[blockR] = self.blockSize - self.blockCount[blockR]
                self.count += self.blockCount[blockR]
                for i in range(R + 1, (blockR + 1) * self.blockSize):
                    if nums1[i] == 0:
                        nums1[i] = 1
                        self.blockCount[blockR] += 1
                        self.count += 1
                    else:
                        nums1[i] = 0
                        self.blockCount[blockR] -= 1
                        self.count -= 1
            else:
                for i in range(blockR * self.blockSize, R + 1):
                    if nums1[i] == 0:
                        nums1[i] = 1
                        self.blockCount[blockR] += 1
                        self.count += 1
                    else:
                        nums1[i] = 0
                        self.blockCount[blockR] -= 1
                        self.count -= 1
            self.isBlockDirty[blockR] = False

        def op2(multiplier):
            self.result += self.count * multiplier

        def op3():
            return self.result

        result = []
        for op, p1, p2 in queries:
            if op == 1:
                op1(p1, p2)
            elif op == 2:
                op2(p1)
            else:
                result.append(op3())
        return result
