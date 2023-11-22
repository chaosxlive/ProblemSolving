class Solution:
    def minLength(self, s: str) -> int:
        while True:
            l = len(s)
            s = ''.join(s.split('AB'))
            s = ''.join(s.split('CD'))
            if l == len(s):
                break
        return len(s)
