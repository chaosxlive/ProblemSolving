# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

class Solution:
    def minSwaps(self, s: str) -> int:
        count = {'0': 0, '1': 0}
        for c in s:
            count[c] += 1
        if count['0'] - count['1'] > 1 or count['1'] - count['0'] > 1:
            return -1

        if count['0'] - count['1'] == 1:
            temp = "01" * count['1'] + "0"
            result = 0
            for i in range(len(s)):
                if temp[i] != s[i]:
                    result += 1
            return result // 2
        elif count['1'] - count['0'] == 1:
            temp = "10" * count['0'] + "1"
            result = 0
            for i in range(len(s)):
                if temp[i] != s[i]:
                    result += 1
            return result // 2
        temp1 = "10" * count['0']
        temp2 = "01" * count['0']
        result1 = result2 = 0
        for i in range(len(s)):
            if temp1[i] != s[i]:
                result1 += 1
            if temp2[i] != s[i]:
                result2 += 1
        return min(result1, result2) // 2
