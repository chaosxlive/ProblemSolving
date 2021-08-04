# https://leetcode.com/problems/three-equal-parts/

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total = arr.count(1)
        if total % 3:
            return [-1, -1]
        if total == 0:
            return [0, 2]

        target = total // 3
        index = count = 0
        seps = []
        while index < len(arr):
            if arr[index]:
                count += 1
                if count in {1, target + 1, 2 * target + 1}:
                    seps.append(index)
                if count in {target, 2 * target, 3 * target}:
                    seps.append(index)
            index += 1

        if not (arr[seps[0]:seps[1] + 1] == arr[seps[2]:seps[3] + 1] == arr[seps[4]:seps[5] + 1]):
            return[-1, -1]
        zero1, zero2, zero3 = seps[2] - seps[1] - 1, seps[4] - seps[3] - 1, len(arr) - seps[5] - 1
        return [-1, -1] if zero1 < zero3 or zero2 < zero3 else [seps[1] + zero3, seps[3] + zero3 + 1]
