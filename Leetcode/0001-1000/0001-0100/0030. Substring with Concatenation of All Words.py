# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from typing import List
from collections import deque


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sLen = len(s)
        wLen = len(words)
        wordLen = len(words[0])
        wholeLen = wordLen * wLen
        expectedCnt = {}
        for word in words:
            if word not in expectedCnt:
                expectedCnt[word] = 0
            expectedCnt[word] += 1
        result = []
        for bias in range(wordLen):
            counter = {word: 0 for word in words}
            validCnt = 0
            if sLen + bias < wholeLen:
                break
            dq = deque()
            for i, _ in enumerate(words[:-1]):
                w = s[i*wordLen+bias:(i+1)*wordLen+bias]
                dq.append(w)
                if w in counter:
                    counter[w] += 1
                    if counter[w] == expectedCnt[w]:
                        validCnt += expectedCnt[w]
                    elif counter[w] == expectedCnt[w] + 1:
                        validCnt -= expectedCnt[w]

            left = bias
            while left + wholeLen <= sLen:
                w = s[left+wholeLen-wordLen:left+wholeLen]
                dq.append(w)
                if w in counter:
                    counter[w] += 1
                    if counter[w] == expectedCnt[w]:
                        validCnt += expectedCnt[w]
                    elif counter[w] == expectedCnt[w] + 1:
                        validCnt -= expectedCnt[w]
                if validCnt == wLen:
                    result.append(left)
                pw = dq.popleft()
                if pw in counter:
                    if counter[pw] == expectedCnt[pw]:
                        validCnt -= expectedCnt[pw]
                    elif counter[pw] == expectedCnt[pw] + 1:
                        validCnt += expectedCnt[pw]
                    counter[pw] -= 1
                left += wordLen

        return result
