# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = []
        prev, index = -1, 0
        direction = 0
        while index < len(dominoes):
            if dominoes[index] == 'L':
                if direction == 1:
                    half = (index - prev) // 2

                    result.append("R" * half)
                    if (index - prev) % 2:
                        result.append(".")
                    result.append("L" * half)

                    prev = index
                    direction = 0
                elif direction == 0:
                    result.append("L" * (index - prev))
                    prev = index
            elif dominoes[index] == 'R':
                if direction:
                    result.append("R" * (index - prev - 1))
                else:
                    result.append("." * (index - prev - 1))
                prev = index - 1
                direction = 1
            index += 1

        if direction == 1:
            result.append("R" * (index - prev - 1))
        else:
            result.append("." * (index - prev - 1))

        return "".join(result)
