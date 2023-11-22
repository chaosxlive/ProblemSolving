# https://leetcode.com/problems/word-search-ii/

class TreeNode:

    def __init__(self, character):
        self.parent = None
        self.character = character
        self.word = None
        self.nextNodes = {}

    def isWord(self):
        return self.word is not None

    def setWord(self, word):
        self.word = word

    def getWord(self):
        return self.word

    def hasAnyNext(self):
        return len(self.nextNodes.keys()) > 0

    def hasNext(self, character):
        return character in self.nextNodes

    def setNext(self, character):
        newNode = TreeNode(character)
        self.nextNodes[character] = newNode
        newNode.parent = self

    def getNext(self, character):
        return self.nextNodes[character]

    def removeNext(self, character):
        del self.nextNodes[character]

    def hasParent(self):
        return self.parent is not None

    def getParent(self):
        return self.parent


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TreeNode('')
        for word in words:
            nodeIterator = root
            for character in word:
                if not nodeIterator.hasNext(character):
                    nodeIterator.setNext(character)
                nodeIterator = nodeIterator.getNext(character)
            nodeIterator.setWord(word)

        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

        def isInRange(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        result = set()
        walked = set()

        def dfs(row, col, nodeIterator):
            walked.add((row, col))
            if nodeIterator.isWord():
                result.add(nodeIterator.getWord())
                nodeIterator.setWord(None)
            for direction in directions:
                nextRow = row + direction[0]
                nextCol = col + direction[1]
                if isInRange(nextRow, nextCol) and not (nextRow, nextCol) in walked:
                    nextCharacter = board[nextRow][nextCol]
                    if nodeIterator.hasNext(nextCharacter):
                        dfs(nextRow, nextCol, nodeIterator.getNext(nextCharacter))
            if nodeIterator.getWord() is None and not nodeIterator.hasAnyNext():
                if nodeIterator.hasParent():
                    parent = nodeIterator.getParent()
                    parent.removeNext(nodeIterator.character)
            walked.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                nodeIterator = root
                if root.hasNext(board[row][col]):
                    dfs(row, col, nodeIterator.getNext(board[row][col]))
        return list(result)
