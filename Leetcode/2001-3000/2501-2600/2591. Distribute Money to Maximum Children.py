# https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money > children * 8:
            return children - 1
        if money == children * 8:
            return children
        money -= children
        eights, rest = divmod(money, 7)
        if rest == 0:
            return eights
        if rest != 3:
            if eights == 0:
                return 0
            return eights
        if eights == children - 1:
            return children - 2
        return eights
