from typing import List, Optional

from sortedcontainers import SortedList


class Solution:

    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = SortedList([nums[0]])
        arr2 = SortedList([nums[1]])
        res1 = [nums[0]]
        res2 = [nums[1]]

        for i in range(2, len(nums)):
            num = nums[i]
            g1 = len(arr1) - arr1.bisect_right(num)
            g2 = len(arr2) - arr2.bisect_right(num)
            if g1 > g2:
                arr1.add(num)
                res1.append(num)
            elif g1 < g2:
                arr2.add(num)
                res2.append(num)
            else:
                if len(arr1) <= len(arr2):
                    arr1.add(num)
                    res1.append(num)
                else:
                    arr2.add(num)
                    res2.append(num)
        return res1 + res2
