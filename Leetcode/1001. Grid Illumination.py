# https://leetcode.com/problems/grid-illumination/

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        isOn = set()
        lightRow, lightCol, lightDiagRT, lightDiagLT = {}, {}, {}, {}
        for lamp in lamps:
            if tuple(lamp) in isOn:
                continue
            isOn.add(tuple(lamp))
            if lamp[0] not in lightRow:
                lightRow[lamp[0]] = 0
            lightRow[lamp[0]] += 1
            if lamp[1] not in lightCol:
                lightCol[lamp[1]] = 0
            lightCol[lamp[1]] += 1
            if lamp[1] - lamp[0] + n not in lightDiagRT:
                lightDiagRT[lamp[1] - lamp[0] + n] = 0
            lightDiagRT[lamp[1] - lamp[0] + n] += 1
            if lamp[0] + lamp[1] not in lightDiagLT:
                lightDiagLT[lamp[0] + lamp[1]] = 0
            lightDiagLT[lamp[0] + lamp[1]] += 1
        result = []
        for query in queries:
            if (query[1] - query[0] + n in lightDiagRT and lightDiagRT[query[1] - query[0] + n] > 0) or\
                    (query[0] in lightRow and lightRow[query[0]] > 0) or\
                    (query[1] in lightCol and lightCol[query[1]] > 0) or\
                    (query[0] + query[1] in lightDiagLT and lightDiagLT[query[0] + query[1]] > 0):
                result.append(1)
            else:
                result.append(0)

            for r in range(-1, 2):
                for c in range(-1, 2):
                    tr, tc = query[0] + r, query[1] + c
                    if 0 <= tr < n and 0 <= tc < n and (tr, tc) in isOn:
                        isOn.remove((tr, tc))
                        lightRow[tr] -= 1
                        lightCol[tc] -= 1
                        lightDiagRT[tc - tr + n] -= 1
                        lightDiagLT[tr + tc] -= 1
        return result
