# https://leetcode.com/contest/biweekly-contest-58/problems/check-if-move-is-legal/

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))
        for R, C in directions:
            r, c = rMove + R, cMove + C
            while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != color and board[r][c] != '.':
                r += R
                c += C
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r, c) != (rMove + R, cMove + C) and board[r][c] != '.':
                return True
        return False
