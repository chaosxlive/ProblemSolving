# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 1
        count = 1
        prev = chars[0]
        while right < len(chars):
            if chars[right] == prev:
                count += 1
                right += 1
            else:
                chars[left] = prev
                left += 1
                if count > 1:
                    temp = str(count)
                    for i, c in enumerate(temp):
                        chars[left + i] = c
                    left += len(temp)
                    count = 1
                prev = chars[right]
                right += 1
        chars[left] = prev
        left += 1
        if count > 1:
            temp = str(count)
            for i, c in enumerate(temp):
                chars[left + i] = c
            left += len(temp)
        return left
