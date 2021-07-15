# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(dirs, visited, board, word, row, col, index):
            if index == len(word):
                return True
            visited.add((row, col))

            for ir, ic in dirs:
                if 0 <= row + ir < len(board) and 0 <= col + ic < len(board[0]) and (row + ir, col + ic) not in visited and board[row + ir][col + ic] == word[index]:
                    visited.add((row + ir, col + ic))
                    if dfs(dirs, visited, board, word, row + ir, col + ic, index + 1):
                        return True
                    visited.remove((row + ir, col + ic))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(dirs, set(), board, word, row, col, 1):
                        return True
        return False
