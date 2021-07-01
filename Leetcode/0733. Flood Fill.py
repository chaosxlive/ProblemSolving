# https://leetcode.com/problems/flood-fill/

from queue import Queue


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        visited.add((sr, sc))
        next = Queue()
        next.put((sr, sc))
        originColor = image[sr][sc]
        while not next.empty():
            row, col = next.get()
            image[row][col] = newColor

            for iR, iC in directions:
                if 0 <= row + iR < len(image) and 0 <= col + iC < len(image[0]) and (row + iR, col + iC) not in visited and image[row + iR][col + iC] == originColor:
                    visited.add((row + iR, col + iC))
                    next.put((row + iR, col + iC))
        return image
