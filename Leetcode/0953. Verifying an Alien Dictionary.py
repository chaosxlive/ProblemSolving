# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        cMap = {c: chr(i + 97) for i, c in enumerate(order)}
        mapped = [''.join(map(lambda x: cMap[x], word)) for word in words]
        return all(mapped[i] <= mapped[i + 1] for i in range(len(mapped) - 1))
