// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

#define MOD 1000000007

int dp[201][2][202];
int temp[201][2][202];

class Solution {
   public:
    int numberOfStableArrays(int zero, int one, int limit) {
        memset(dp, 0, sizeof(dp));
        dp[1][0][1] = 1;
        dp[0][1][1] = 1;
        dp[1][0][limit + 1] = 1;
        dp[0][1][limit + 1] = 1;

        for (int l = 2; l <= zero + one; l++) {
            memset(temp, 0, sizeof(temp));
            for (int prev = 0; prev <= zero; prev++) {
                for (int lmt = 1; lmt <= limit; lmt++) {
                    if (lmt == 1) {
                        if (prev > 0) {
                            temp[prev][0][lmt] = dp[prev - 1][1][limit + 1];
                        }
                        temp[prev][1][lmt] = dp[prev][0][limit + 1];
                    } else {
                        if (prev > 0) {
                            temp[prev][0][lmt] = dp[prev - 1][0][lmt - 1];
                        }
                        temp[prev][1][lmt] = dp[prev][1][lmt - 1];
                    }
                    temp[prev][0][limit + 1] = (temp[prev][0][limit + 1] + temp[prev][0][lmt]) % MOD;
                    temp[prev][1][limit + 1] = (temp[prev][1][limit + 1] + temp[prev][1][lmt]) % MOD;
                }
            }
            for (int i = 0; i < 201; i++) {
                for (int j = 0; j < 2; j++) {
                    for (int k = 0; k < 202; k++) {
                        dp[i][j][k] = temp[i][j][k];
                    }
                }
            }
        }
        return (dp[zero][0][limit + 1] + dp[zero][1][limit + 1]) % MOD;
    }
};