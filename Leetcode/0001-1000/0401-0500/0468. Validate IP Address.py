# https://leetcode.com/problems/validate-ip-address/

class Solution:
    def validIPAddress(self, IP: str) -> str:

        def isIPv4(ip: str) -> bool:
            part = ip.split('.')
            if len(part) != 4:
                return False
            for p in part:
                for c in p:
                    if not '0' <= c <= '9':
                        return False
                if (len(p) > 1 and p[0] == '0') or (len(p) == 0) or (not 0 <= int(p) <= 255):
                    return False
            return True

        def isIPv6(ip: str) -> bool:
            part = ip.lower().split(':')
            if len(part) != 8:
                return False
            for p in part:
                for c in p:
                    if not ('0' <= c <= '9' or 'a' <= c <= 'f'):
                        return False
                if len(p) == 0 or len(p) > 4:
                    return False
            return True

        if isIPv4(IP):
            return "IPv4"
        elif isIPv6(IP):
            return "IPv6"
        return "Neither"
