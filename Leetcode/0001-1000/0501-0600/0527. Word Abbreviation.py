# https://leetcode.com/problems/word-abbreviation/

from collections import defaultdict
from typing import List


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        abbrMap = defaultdict(list)
        delList = set()
        needExpand = set()
        for word in words:
            abbrKey = (word[0], len(word) - 2, word[-1])
            abbrMap[abbrKey].append(word)
            if len(abbrMap[abbrKey]) > 1:
                needExpand.add(abbrKey)
                delList.add(abbrKey)

        while len(needExpand):
            nextNeedExpand = set()
            for abbrKey in needExpand:
                abbrWords = abbrMap[abbrKey]
                for word in abbrWords:
                    newAbbrKey = (abbrKey[0] + word[len(abbrKey[0])], abbrKey[1] - 1, abbrKey[2])
                    abbrMap[newAbbrKey].append(word)
                    if len(abbrMap[newAbbrKey]) > 1:
                        nextNeedExpand.add(newAbbrKey)
                        delList.add(newAbbrKey)
            needExpand = nextNeedExpand

        wordMap = {}
        for abbrKey, abbrWords in abbrMap.items():
            if len(abbrWords) > 1:
                continue
            wordMap[abbrWords[0]] = abbrKey

        result = []
        for word in words:
            pre, cnt, suf = wordMap[word]
            if cnt < 2:
                result.append(word)
            else:
                result.append(f'{pre}{cnt}{suf}')

        return result
