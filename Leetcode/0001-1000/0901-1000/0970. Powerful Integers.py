# https://leetcode.com/problems/powerful-integers/

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1 and y == 1:
            return [] if bound <= 1 else [2]
        if x == 1:
            iterN = 0
            result = []
            while True:
                temp = y ** iterN + 1
                if temp <= bound:
                    result.append(temp)
                else:
                    break
                iterN += 1
            return result
        if y == 1:
            iterN = 0
            result = []
            while True:
                temp = x ** iterN + 1
                if temp <= bound:
                    result.append(temp)
                else:
                    break
                iterN += 1
            return result
        result = set()
        iterX = 0
        while True:
            iterY = 0
            while True:
                temp = x ** iterX + y ** iterY
                if temp <= bound:
                    result.add(temp)
                else:
                    break
                iterY += 1
            if x ** iterX + 1 > bound:
                break
            iterX += 1

        return list(result)
