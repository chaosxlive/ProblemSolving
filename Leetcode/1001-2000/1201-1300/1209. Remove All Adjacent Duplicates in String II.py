# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_stack = []
        count_stack = []

        for c in s:
            if len(char_stack) == 0 or c != char_stack[-1]:
                char_stack.append(c)
                count_stack.append(1)
            else:
                count_stack[-1] += 1
                if count_stack[-1] >= k:
                    count_stack[-1] -= k
                    if count_stack[-1] == 0:
                        char_stack.pop()
                        count_stack.pop()
                        
        result = ""
        for i in range(len(char_stack)):
            result += char_stack[i] * count_stack[i]

        return result