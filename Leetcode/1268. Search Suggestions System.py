# https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products, searchWord: str):
        products.sort()
        result = []
        index = 0
        while index < len(searchWord):
            i = 0
            while i < len(products):
                if index >= len(products[i]) or searchWord[index] != products[i][index]:
                    del products[i]
                else:
                    i += 1
            result.append(products[:3])
            index += 1
        return result
