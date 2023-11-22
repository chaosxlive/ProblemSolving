# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        index1 = ptr1 = 0
        index2 = ptr2 = 0
        while True:
            if ptr1 == len(word1[index1]):
                ptr1 = 0
                index1 += 1
            if ptr2 == len(word2[index2]):
                ptr2 = 0
                index2 += 1

            if index1 == len(word1) or index2 == len(word2):
                if index1 == len(word1) and index2 == len(word2):
                    return True
                else:
                    return False
            
            if word1[index1][ptr1] != word2[index2][ptr2]:
                return False
                
            ptr1 += 1
            ptr2 += 1