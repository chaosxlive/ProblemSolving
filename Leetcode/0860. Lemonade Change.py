# https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = count10 = 0
        for bill in bills:
            if bill == 20:
                if count5 == 0 or (count10 == 0 and count5 < 3):
                    return False
                if count10 == 0:
                    count5 -= 3
                else:
                    count5 -= 1
                    count10 -= 1
            elif bill == 10:
                if count5 == 0:
                    return False
                count5 -= 1
                count10 += 1
            else:
                count5 += 1
        return True
