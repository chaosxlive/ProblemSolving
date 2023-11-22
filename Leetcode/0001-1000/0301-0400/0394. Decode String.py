# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        prev = 0
        index = 0
        times = 0
        countP = 0
        status = 0  # 0: alphabet, 1: number, 2: nested
        while index < len(s):
            if status == 0:
                if '0' <= s[index] <= '9':
                    result.append(s[prev:index])
                    prev = index
                    status = 1
            elif status == 1:
                if s[index] == '[':
                    times = int(s[prev:index])
                    prev = index + 1
                    status = 2
            else:
                if s[index] == '[':
                    countP += 1
                elif s[index] == ']':
                    if countP == 0:
                        result.append(self.decodeString(s[prev:index]) * times)
                        prev = index + 1
                        status = 0
                    else:
                        countP -= 1
            index += 1
        result.append(s[prev:index])
        return "".join(result)
