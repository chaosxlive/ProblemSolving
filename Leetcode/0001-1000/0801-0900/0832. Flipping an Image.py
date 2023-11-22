# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = [[] for row in range(len(image))]

        for row in range(len(image)):
            for col in image[row][::-1]:
                result[row].append(1 if col == 0 else 0)
        return result