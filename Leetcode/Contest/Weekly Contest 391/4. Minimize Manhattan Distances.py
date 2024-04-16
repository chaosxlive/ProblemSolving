from math import inf
from typing import List, Optional


class Solution:

    def minimumDistance(self, points: List[List[int]]) -> int:
        XS = sorted(map(tuple, points))
        YS = sorted(map(tuple, points), key=lambda x: (x[1], x[0]))
        L = len(points)
        result = inf

        minsum = maxsum = points[0][0] + points[0][1]
        mindiff = maxdiff = points[0][0] - points[0][1]
        minsumi = maxsumi = mindiffi = maxdiffi = 0
        for i in range(1, L):
            sum = points[i][0] + points[i][1]
            diff = points[i][0] - points[i][1]
            if (sum < minsum):
                minsum = sum
                minsumi = i
            elif (sum > maxsum):
                maxsum = sum
                maxsumi = i
            if (diff < mindiff):
                mindiff = diff
                mindiffi = i
            elif (diff > maxdiff):
                maxdiff = diff
                maxdiffi = i

        result = max(maxsum - minsum, maxdiff - mindiff)
        print([minsumi, maxsumi, mindiffi, maxdiffi])

        for ignore in [minsumi, maxsumi, mindiffi, maxdiffi]:
            start = 1 if ignore == 0 else 0
            minsum = maxsum = points[start][0] + points[start][1]
            mindiff = maxdiff = points[start][0] - points[start][1]
            for i in range(1, L):
                if i == ignore:
                    continue
                sum = points[i][0] + points[i][1]
                diff = points[i][0] - points[i][1]
                if (sum < minsum):
                    minsum = sum
                elif (sum > maxsum):
                    maxsum = sum
                if (diff < mindiff):
                    mindiff = diff
                elif (diff > maxdiff):
                    maxdiff = diff

            result = min(result, max(maxsum - minsum, maxdiff - mindiff))

        return result


# print(Solution().minimumDistance([[3, 10], [5, 15], [10, 2], [4, 4]]))  # 12
# print(Solution().minimumDistance([[1, 1], [1, 1], [1, 1]]))  # 12
# print(Solution().minimumDistance([[10, 3], [4, 2], [8, 9], [9, 3], [4, 5], [6, 9], [9, 2], [7, 5]]))  # 10