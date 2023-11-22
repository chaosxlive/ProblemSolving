# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prevFlower = 0
        while prevFlower < len(flowerbed) and flowerbed[prevFlower] != 1:
            prevFlower += 1
        space = prevFlower // 2
        if space >= n:
            return True
        if prevFlower == len(flowerbed):
            return (prevFlower + 1) // 2 >= n
        for f in range(prevFlower + 2, len(flowerbed)):
            if flowerbed[f] == 1:
                space += (f - prevFlower - 2) // 2
                if space >= n:
                    return True
                prevFlower = f
        space += (len(flowerbed) - prevFlower - 1) // 2
        return space >= n
