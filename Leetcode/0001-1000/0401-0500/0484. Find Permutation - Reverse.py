# https://leetcode.com/problems/find-permutation/

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        l = len(s)
        result = [i for i in range(1, l + 2)]
        ptr = left = right = 0
        while ptr < l:
            if s[ptr] == 'D':
                left = ptr
                right = ptr + 1
                while right < l and s[right] == 'D':
                    right += 1
                result[left:right + 1] = reversed(result[left:right + 1])
                ptr = right - 1
            ptr += 1
        return result
