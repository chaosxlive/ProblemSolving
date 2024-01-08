# https://leetcode.com/problems/palindrome-rearrangement-queries/

from bisect import bisect_right
from typing import List


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        sLen = len(s)
        qLen = len(queries)
        sHalfLen = sLen // 2
        s1, s2 = s[:sHalfLen], s[-1:sHalfLen-1:-1]

        diffIdxs = [i for i in range(sHalfLen) if s1[i] != s2[i]]

        count1 = [[0] * 26]
        count2 = [[0] * 26]
        ord_a = ord('a')
        for i in range(sHalfLen):
            count1.append(count1[-1][:])
            count2.append(count2[-1][:])
            count1[-1][ord(s1[i]) - ord_a] += 1
            count2[-1][ord(s2[i]) - ord_a] += 1

        if not diffIdxs:
            return [True] * len(queries)

        def isRangeSame(start, end):
            for i in range(26):
                if count1[end + 1][i] - count1[start][i] != count2[end + 1][i] - count2[start][i]:
                    return False
            return True

        def checkIntersectChars(ll, lr, rl, rr):
            cnt1, cnt2 = count1, count2
            if rl < ll:
                ll, lr, rl, rr = rl, rr, ll, lr
                cnt1, cnt2 = cnt2, cnt1
            if lr >= rr:
                return isRangeSame(ll, lr)
            if rl <= ll:
                return isRangeSame(rl, rr)

            if not isRangeSame(min(ll, rl), max(lr, rr)):
                return False

            for i in range(26):
                if cnt1[lr + 1][i] - cnt1[ll][i] < cnt2[rl][i] - cnt2[ll][i]:
                    return False
                if cnt2[rr + 1][i] - cnt2[rl][i] < cnt1[rr + 1][i] - cnt1[lr + 1][i]:
                    return False
            return True

        def checkCover(ll, lr, rl, rr):
            if rl < ll:
                ll, lr, rl, rr = rl, rr, ll, lr

            if rl <= lr:
                return not (min(ll, rl) > diffIdxs[0] or max(lr, rr) < diffIdxs[-1])

            if ll > diffIdxs[0] or rr < diffIdxs[-1]:
                return False

            pos = bisect_right(diffIdxs, lr)
            return not (pos < len(diffIdxs) and diffIdxs[pos] < rl)

        result = [False] * qLen
        for i, [ll, lr, rl, rr] in enumerate(queries):
            rl, rr = sLen - rr - 1, sLen - rl - 1,

            if not checkCover(ll, lr, rl, rr):
                continue

            if lr < rl or rr < ll:
                result[i] = isRangeSame(ll, lr) and isRangeSame(rl, rr)
                continue

            result[i] = checkIntersectChars(ll, lr, rl, rr)

        return result
