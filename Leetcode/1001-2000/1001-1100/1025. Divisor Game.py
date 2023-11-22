# https://leetcode.com/problems/divisor-game/

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

# 1 will lose
# 2 will win   # 2 can only go to 1
# 3 will lose  # 3 can only go to 2
# 4 will win   # 4 can go to 3 to win
# ...
# So we can know that the odd number will always go to even first,
# so all odd number will lose. In the other side, even number can
# always choose factor 1 to a odd number, so all even number will win.