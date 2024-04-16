# https://leetcode.com/problems/bag-of-tokens/

from typing import List


class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens.sort()

        left, right = 0, len(tokens) - 1
        score = 0
        result = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                result = max(result, score)
                left += 1
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return result
