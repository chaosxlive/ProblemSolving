# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        dists = [[0, 0] for i in range(len(arr))]
        prevLarger = []
        for i in range(len(arr)):
            if len(prevLarger) == 0 or arr[i] > arr[prevLarger[-1]]:
                prevLarger.append(i)
            else:
                while len(prevLarger) > 0 and arr[i] <= arr[prevLarger[-1]]:
                    prevLarger.pop()
                dists[i][0] = i - prevLarger[-1] - 1 if len(prevLarger) else i
                prevLarger.append(i)
        prevLarger.clear()
        for i in range(len(arr) - 1, -1, -1):
            if len(prevLarger) == 0 or arr[i] >= arr[prevLarger[-1]]:
                prevLarger.append(i)
            else:
                while len(prevLarger) > 0 and arr[i] < arr[prevLarger[-1]]:
                    prevLarger.pop()
                dists[i][1] = prevLarger[-1] - i - 1 if len(prevLarger) else len(arr) - i - 1
                prevLarger.append(i)
        result = 0
        for idx, [left, right] in enumerate(dists):
            result += (left + 1) * (right + 1) * arr[idx]
        return result % 1000000007
