MOD = 10**9 + 7


class Solution:

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        dp = [[[0 for cont in range(202)] for prev in range(2)] for zCnt in range(201)]
        dp[1][0][1] = 1
        dp[0][1][1] = 1
        dp[1][0][limit + 1] = 1
        dp[0][1][limit + 1] = 1

        for l in range(2, zero + one + 1):
            temp = [[[0 for cont in range(202)] for prev in range(2)] for zCnt in range(201)]
            for prev in range(zero + 1):
                for lmt in range(1, limit + 1):
                    if lmt == 1:
                        if prev > 0:
                            temp[prev][0][lmt] = dp[prev - 1][1][limit + 1]
                        temp[prev][1][lmt] = dp[prev][0][limit + 1]
                    else:
                        if prev > 0:
                            temp[prev][0][lmt] = dp[prev - 1][0][lmt - 1]
                        temp[prev][1][lmt] = dp[prev][1][lmt - 1]
                    temp[prev][0][limit + 1] = (temp[prev][0][limit + 1] + temp[prev][0][lmt]) % MOD
                    temp[prev][1][limit + 1] = (temp[prev][1][limit + 1] + temp[prev][1][lmt]) % MOD
            dp = temp
        return (dp[zero][0][limit + 1] + dp[zero][1][limit + 1]) % MOD


# print(Solution().numberOfStableArrays(1, 1, 2)) # 2
# print(Solution().numberOfStableArrays(1, 2, 1)) # 1
# print(Solution().numberOfStableArrays(3, 3, 2)) # 14
# print(Solution().numberOfStableArrays(2, 2, 1))  # 2
# print(Solution().numberOfStableArrays(1, 4, 1))  # 0
# print(Solution().numberOfStableArrays(1, 2, 1))  # 1
# print(Solution().numberOfStableArrays(1, 3, 1))  # 0
# print(Solution().numberOfStableArrays(1, 6, 3))  # 1
