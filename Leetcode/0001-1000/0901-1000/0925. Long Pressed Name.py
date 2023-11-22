# https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]:
            return False
        indexName = indexTyped = 1
        while indexName < len(name) and indexTyped < len(typed):
            if name[indexName] == typed[indexTyped]:
                indexName += 1
                indexTyped += 1
            else:
                prevChar = typed[indexTyped - 1]
                if typed[indexTyped] != prevChar:
                    return False
                else:
                    while indexTyped < len(typed) and typed[indexTyped] == prevChar:
                        indexTyped += 1
        if indexName < len(name) and indexTyped >= len(typed):
            return False
        while indexTyped < len(typed) and typed[indexTyped] == name[-1]:
            indexTyped += 1
        return indexTyped == len(typed)