# https://leetcode.com/problems/beautiful-array/

class Solution:
    def beautifulArray(self, N):
        history = {1: [1]}

        def find(num):
            if num not in history:
                odds = find((num + 1) // 2)
                evens = find(num // 2)
                history[num] = [2 * odd - 1 for odd in odds] + [2 * even for even in evens]
            return history[num]

        return find(N)
