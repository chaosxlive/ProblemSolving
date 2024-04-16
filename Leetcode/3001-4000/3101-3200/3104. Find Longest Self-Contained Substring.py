# https://leetcode.com/problems/find-longest-self-contained-substring/


class Solution:

    def maxSubstringLength(self, s: str) -> int:
        firstSeen = {}
        lastSeen = {}
        result = -1
        for i, c in enumerate(s):
            if c not in firstSeen:
                firstSeen[c] = i
            lastSeen[c] = i
        firstLen = 0
        prevStart = -1
        prevLen = 0
        prevEnd = -1
        for c, i in sorted(firstSeen.items(), key=lambda x: x[1]):
            if prevStart <= i <= prevEnd:
                continue
            start = i
            end = lastSeen[c]
            isInvalid = False
            while i < end:
                if firstSeen[s[i]] < start:
                    isInvalid = True
                    break
                end = max(end, lastSeen[s[i]])
                i += 1
            if isInvalid:
                prevLen = 0
                firstLen = 0
                continue
            if start != prevEnd + 1:
                prevLen = 0
            if prevLen + end - start + 1 == len(s):
                if firstLen > 0:
                    result = max(result, prevLen + end - start + 1 - firstLen)
                else:
                    isInvalid = True
            else:
                result = max(result, prevLen + end - start + 1)
                if firstLen == 0:
                    firstLen = end - start + 1
            prevLen += end - start + 1
            if not isInvalid:
                if prevStart == -1:
                    prevStart = start
                prevEnd = end
        return result

