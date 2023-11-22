# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sheet = set()
        for n in arr:
            if n in sheet:
                return True
            if n % 2 == 0:
                sheet.add(n // 2)
            sheet.add(2 * n)
        return False