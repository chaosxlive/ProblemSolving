# https://leetcode.com/problems/design-compressed-string-iterator/

class StringIterator:

    def __init__(self, compressedString: str):
        self.string = compressedString
        self.stringPtr = 0
        self.charIdx = -1
        self.charTotal = 0
        self.count = 0

    def next(self) -> str:
        if self.count == self.charTotal:
            if self.stringPtr < len(self.string):
                self.charIdx = self.stringPtr
                self.stringPtr += 1
                self.charTotal = 0
                while self.stringPtr < len(self.string) and ord('0') <= ord(self.string[self.stringPtr]) <= ord('9'):
                    self.charTotal = 10 * self.charTotal + int(self.string[self.stringPtr])
                    self.stringPtr += 1
                self.count = 1
                return self.string[self.charIdx]
            else:
                return ' '
        else:
            self.count += 1
            return self.string[self.charIdx]

    def hasNext(self) -> bool:
        nextChar = self.next()
        if nextChar == ' ':
            return False
        self.count -= 1
        return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
