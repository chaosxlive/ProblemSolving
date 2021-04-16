# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def __init__(self) -> None:
        self.alphabet = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8
        }

    def squareIsWhite(self, coordinates: str) -> bool:
        return (self.alphabet[coordinates[0]] + int(coordinates[1])) % 2
