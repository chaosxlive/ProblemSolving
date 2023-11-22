# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split(' ')
        prev = 0
        for token in tokens:
            try:
                num = int(token)
                if num <= prev:
                    return False
                prev = num
            except:
                pass
        return True
