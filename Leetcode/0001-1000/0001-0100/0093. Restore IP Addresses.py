# https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        for len1 in range(1, 4):
            for len2 in range(1, 4):
                for len3 in range(1, 4):
                    len4 = len(s) - len1 - len2 - len3
                    if 1 <= len4 <= 3:
                        part1 = s[:len1]
                        if (len(part1) != 1 and part1[0] == '0') or (int(part1) > 255):
                            continue
                        part2 = s[len1:len1 + len2]
                        if (len(part2) != 1 and part2[0] == '0') or (int(part2) > 255):
                            continue
                        part3 = s[-len3 - len4:-len4]
                        if (len(part3) != 1 and part3[0] == '0') or (int(part3) > 255):
                            continue
                        part4 = s[-len4:]
                        if (len(part4) != 1 and part4[0] == '0') or (int(part4) > 255):
                            continue
                        result.append(part1 + '.' + part2 + '.' + part3 + '.' + part4)
        return result
