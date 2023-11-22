# https://leetcode.com/problems/word-ladder-ii/

from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        container = defaultdict(set)
        words = set(wordList)

        if endWord not in words:
            return []

        isFound, isReverse = False, False
        begins, ends, current = set([beginWord]), set([endWord]), set()
        while begins and not isFound:
            words -= begins
            for begin in begins:
                for possible in [begin[:i] + c + begin[i + 1:] for i in range(len(begin)) for c in "abcdefghijklmnopqrstuvwxyz"]:
                    if possible in words:
                        if possible in ends:
                            isFound = True
                        else:
                            current.add(possible)
                        if isReverse:
                            container[possible].add(begin)
                        else:
                            container[begin].add(possible)
            begins, current = current, set()
            if len(begins) > len(ends):
                begins, ends, isReverse = ends, begins, not isReverse

        def backtrack(word):
            return [[word]] if word == endWord else [[word] + others for w in container[word] for others in backtrack(w)]
        return backtrack(beginWord)
