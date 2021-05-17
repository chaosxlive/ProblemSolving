# https://leetcode.com/contest/weekly-contest-241/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count1, self.count2 = {}, {}
        for num in nums1:
            if num not in self.count1:
                self.count1[num] = 0
            self.count1[num] += 1
        for num in nums2:
            if num not in self.count2:
                self.count2[num] = 0
            self.count2[num] += 1

    def add(self, index: int, val: int) -> None:
        self.count2[self.nums2[index]] -= 1
        self.nums2[index] += val
        if self.nums2[index] not in self.count2:
            self.count2[self.nums2[index]] = 0
        self.count2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        result = 0
        for key in self.count1.keys():
            if tot - key in self.count2:
                result += self.count1[key] * self.count2[tot - key]
        return result


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
