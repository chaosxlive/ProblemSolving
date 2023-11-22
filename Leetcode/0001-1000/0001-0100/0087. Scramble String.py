# https://leetcode.com/problems/scramble-string/

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def divide(s1, s2):
            if s1 == s2:
                return True

            if (s1, s2) in memo:
                return memo[s1, s2]

            if len(s1) == 1:
                return s1 == s2

            if sorted(s1) != sorted(s2):
                memo[s1, s2] = False
                return False

            for pos in range(1, len(s1)):

                left = s1[:pos]
                right = s1[pos:]

                swap = divide(left, s2[-pos:]) and divide(right, s2[:-pos])

                if swap:
                    memo[left, s2[-pos:]] = True
                    memo[right, s2[:-pos]] = True
                    return True

                no_swap = divide(left, s2[:pos]) and divide(right, s2[pos:])

                if no_swap:
                    memo[left, s2[:pos]] = True
                    memo[right, s2[pos:]] = True
                    return True

            memo[s1, s2] = False
            return False

        return divide(s1, s2)
