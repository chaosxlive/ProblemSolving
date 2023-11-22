# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        dists = [0 for i in range(len(arr))]
        prevLarger = []
        for i in range(len(arr)):
            if len(prevLarger) == 0 or arr[i] > arr[prevLarger[-1]]:
                prevLarger.append(i)
            else:
                while len(prevLarger) > 0 and arr[i] <= arr[prevLarger[-1]]:
                    prevLarger.pop()
                dists[i] = i - prevLarger[-1] - 1 if len(prevLarger) else i
                prevLarger.append(i)
        prevLarger.clear()
        result = 0
        for i in range(len(arr) - 1, -1, -1):
            left, right = dists[i], 0
            if len(prevLarger) == 0 or arr[i] >= arr[prevLarger[-1]]:
                prevLarger.append(i)
            else:
                while len(prevLarger) > 0 and arr[i] < arr[prevLarger[-1]]:
                    prevLarger.pop()
                right = prevLarger[-1] - i - 1 if len(prevLarger) else len(arr) - i - 1
                prevLarger.append(i)
            result += (left + 1) * (right + 1) * arr[i]
        return result % 1000000007
