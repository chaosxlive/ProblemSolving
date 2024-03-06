class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if l[left] != l[right]:
                l[left] = l[right] = l[left] if ord(l[left]) < ord(l[right]) else l[right]
            left += 1
            right -= 1
        return ''.join(l)