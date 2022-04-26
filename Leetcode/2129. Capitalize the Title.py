# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(map(lambda x: x.lower() if len(x) <= 2 else x.capitalize(), title.split(' ')))
