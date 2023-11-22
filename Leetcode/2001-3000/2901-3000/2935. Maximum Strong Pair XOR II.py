# https://leetcode.com/problems/maximum-strong-pair-xor-ii/

from typing import List


class Node:
    def __init__(self, num=2147483647) -> None:
        self.bitZero = None
        self.bitOne = None
        self.min = num
        self.max = num


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        root = Node()
        for num in nums:
            bitMask = 1 << 22
            nodeIter = root
            while bitMask > 0:
                if num & bitMask == 0:
                    if nodeIter.bitZero is None:
                        nodeIter.bitZero = Node(num)
                    nodeIter.min = min(nodeIter.min, num)
                    nodeIter.max = max(nodeIter.max, num)
                    nodeIter = nodeIter.bitZero
                else:
                    if nodeIter.bitOne is None:
                        nodeIter.bitOne = Node(num)
                    nodeIter.min = min(nodeIter.min, num)
                    nodeIter.max = max(nodeIter.max, num)
                    nodeIter = nodeIter.bitOne
                bitMask >>= 1

        result = 0
        for num in nums:
            bitMask = 1 << 22
            nodeIter = root
            while bitMask > 0:
                if nodeIter.bitZero is None and nodeIter.bitOne is None:
                    break
                if nodeIter.bitZero is None:
                    nodeIter = nodeIter.bitOne
                    bitMask >>= 1
                    continue
                if nodeIter.bitOne is None:
                    nodeIter = nodeIter.bitZero
                    bitMask >>= 1
                    continue

                curBit = num & bitMask
                if curBit == 0:
                    if abs(nodeIter.bitOne.max - num) > min(nodeIter.bitOne.max, num) and abs(nodeIter.bitOne.min - num) > min(nodeIter.bitOne.min, num):
                        nodeIter = nodeIter.bitZero
                    else:
                        nodeIter = nodeIter.bitOne
                else:
                    if abs(nodeIter.bitZero.max - num) > min(nodeIter.bitZero.max, num) and abs(nodeIter.bitZero.min - num) > min(nodeIter.bitZero.min, num):
                        nodeIter = nodeIter.bitOne
                    else:
                        nodeIter = nodeIter.bitZero
                bitMask >>= 1
            result = max(result, nodeIter.min ^ num)
        return result
