# https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0
        while True:
            if bits[index] == 1:
                index += 2
                if index == len(bits):
                    return False
            else:
                index += 1
                if index == len(bits):
                    return True
