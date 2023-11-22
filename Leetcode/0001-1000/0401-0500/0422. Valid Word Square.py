# https://leetcode.com/problems/valid-word-square/

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        try:
            for row in range(len(words)):
                for col in range(len(words[row])):
                    if words[row][col] != words[col][row]:
                        return False
            return True
        except Exception:
            return False
