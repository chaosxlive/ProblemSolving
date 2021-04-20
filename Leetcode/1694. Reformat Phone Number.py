# https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        strip = number.replace(' ', '').replace('-', '')
        i = 0
        result = ""
        while i * 3 + 4 < len(strip):
            result += strip[i * 3: i * 3 + 3] + '-'
            i += 1
        if len(strip) - i * 3 == 2:
            result += strip[i * 3: i * 3 + 2]
        elif len(strip) - i * 3 == 3:
            result += strip[i * 3: i * 3 + 3]
        else:
            result += strip[i * 3: i * 3 + 2] + '-' + strip[i * 3 + 2: i * 3 + 4]
        return result

