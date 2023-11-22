# https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = {}
        self.suffix = {}
        seen = set()
        for index in range(len(words) - 1, -1, -1):
            word = words[index]
            if word in seen:
                continue
            seen.add(word)
            for subIndex in range(len(word) + 1):
                if word[:subIndex] not in self.prefix:
                    self.prefix[word[:subIndex]] = set()
                self.prefix[word[:subIndex]].add(index)
                if word[subIndex:] not in self.suffix:
                    self.suffix[word[subIndex:]] = set()
                self.suffix[word[subIndex:]].add(index)

    def f(self, prefix: str, suffix: str) -> int:
        a = self.prefix[prefix]
        b = self.suffix[suffix]
        result = a & b
        return max(result) if result else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
