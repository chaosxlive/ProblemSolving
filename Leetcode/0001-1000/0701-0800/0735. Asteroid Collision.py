# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            if asteroid > 0:
                result.append(asteroid)
            else:
                while True:
                    if len(result) == 0 or result[-1] < 0:
                        result.append(asteroid)
                        break
                    if asteroid + result[-1] > 0:
                        break
                    elif asteroid + result[-1] < 0:
                        result.pop()
                    else:
                        result.pop()
                        break
        return result

