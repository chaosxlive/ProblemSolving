# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if idKey == self.ptr:
            index = idKey
            result = []
            while index < len(self.stream) and self.stream[index] != None:
                result.append(self.stream[index])
                index += 1
            self.ptr = index
            return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
