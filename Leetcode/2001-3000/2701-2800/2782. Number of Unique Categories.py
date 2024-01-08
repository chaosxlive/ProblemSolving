# https://leetcode.com/problems/number-of-unique-categories/

from typing import Optional


# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass


class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        uniques = [0]
        for i in range(1, n):
            isNew = True
            for u in uniques:
                if categoryHandler.haveSameCategory(i, u):
                    isNew = False
                    break
            if isNew:
                uniques.append(i)
        return len(uniques)
