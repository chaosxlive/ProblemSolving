# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        count = indexSum = 0
        left, right, result = [], [], []
        for index in range(len(boxes)):
            if boxes[index] == '1':
                count += 1
                indexSum += index
        left.append(1 if boxes[0] == '1' else 0)
        right.append(count)
        result.append(indexSum)

        for index in range(1, len(boxes)):
            left.append(left[-1] + (1 if boxes[index] == '1' else 0))
            right.append(count - left[-1] + (1 if boxes[index] == '1' else 0))
            result.append(result[-1] + left[-2] - right[-1])

        return result


# count = 3 => right[0]
# indexSum = 11 => result[0]
# left[i] = left[i - 1] + 1 if boxes[i] == '1' else left[i - 1]
# right[i] + left[i] = count + 1 if boxes[i] == 1 else count
# result[i] = result[i - 1] + left[i - 1] - right[i]
#
# index  | 0  1 2 3 4 5
# boxes  | 0  0 1 0 1 1
# -------+--------------
# left   | 0  0 1 1 2 3
# right  | 3  3 3 2 2 1
# result | 11 8 5 4 3 4
