# https://leetcode.com/problems/design-a-text-editor/

class TextEditor:

    def __init__(self):
        self.textLeft = ''
        self.textRight = ''

    def addText(self, text: str) -> None:
        self.textLeft = self.textLeft + text

    def deleteText(self, k: int) -> int:
        lengthTextLeft = len(self.textLeft)
        if lengthTextLeft <= k:
            self.textLeft = ''
            self.cursorPos = 0
            return lengthTextLeft
        self.textLeft = self.textLeft[:-k]
        return k

    def cursorLeft(self, k: int) -> str:
        movedText = self.textLeft[-k:]
        self.textLeft = self.textLeft[:-k]
        self.textRight = movedText + self.textRight
        return self.textLeft[-10:]

    def cursorRight(self, k: int) -> str:
        movedText = self.textRight[:k]
        self.textLeft = self.textLeft + movedText
        self.textRight = self.textRight[k:]
        return self.textLeft[-10:]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
