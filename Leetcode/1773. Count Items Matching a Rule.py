# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "type":
            for item in items:
                if item[0] == ruleValue:
                    count += 1
        elif ruleKey == "color":
            for item in items:
                if item[1] == ruleValue:
                    count += 1
        elif ruleKey == "name":
            for item in items:
                if item[2] == ruleValue:
                    count += 1
        
        return count
            