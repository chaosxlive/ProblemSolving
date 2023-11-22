# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        bit = False
        while N != 0:
            if (K - 1) & (1 << N - 1):
                bit = not bit
            N -= 1
            
        return 1 if bit else  0