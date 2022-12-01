# https://leetcode.com/problems/erect-the-fence/

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        def crossProduct(o, p1, p2):
            v1X = p1[0] - o[0]
            v1Y = p1[1] - o[1]
            v2X = p2[0] - o[0]
            v2Y = p2[1] - o[1]
            return v1X * v2Y - v1Y * v2X

        def calcHalfHull(points):
            stack = []
            for point in points:
                while len(stack) >= 2 and crossProduct(stack[-2], stack[-1], point) > 0:
                    stack.pop()
                stack.append(tuple(point))
            return stack

        trees.sort()
        set1 = calcHalfHull(trees)
        set2 = calcHalfHull(trees[::-1])
        return list(set(set1 + set2))
