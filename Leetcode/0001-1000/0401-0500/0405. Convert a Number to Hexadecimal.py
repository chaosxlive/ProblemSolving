# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_char = "0123456789abcdef"
        index = 0
        ans = ""
        while index < 8 and num != 0:
            ans = hex_char[num & 0xf] + ans
            num >>= 4 
            index += 1
        return ans