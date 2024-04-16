# https://leetcode.com/problems/split-array-into-fibonacci-sequence/

from typing import List


class Solution:

    def splitIntoFibonacci(self, num: str) -> List[int]:
        result = []
        for l1 in range(1, len(num) - 2):
            if num[0] == 0 and l1 > 1:
                return []
            n1 = int(num[:l1])
            if n1 >= 2**31:
                break
            result.append(n1)
            for l2 in range(1, len(num) - l1 - 1):
                if num[l1] == 0 and l2 > 1:
                    break
                n2 = int(num[l1:l1 + l2])
                if n2 >= 2**31:
                    break
                result.append(n2)
                ptr = l1 + l2
                while ptr < len(num):
                    prev = result[-2] + result[-1]
                    if prev >= 2**31:
                        break
                    pred = str(prev)
                    if num[ptr:ptr + len(pred)] == pred:
                        result.append(prev)
                        ptr += len(pred)
                    else:
                        break
                if ptr == len(num):
                    return result if len(result) > 2 else []
                while len(result) > 1:
                    result.pop()
            result.pop()
        return []
