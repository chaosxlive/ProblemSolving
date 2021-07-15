// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   private:
    int prefixSum[101][101];

   public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        for (int row = 0; row < matrix.size(); row++) {
            for (int col = 0; col < matrix[0].size(); col++) {
                prefixSum[row + 1][col + 1] = matrix[row][col] - prefixSum[row][col] + prefixSum[row][col + 1] + prefixSum[row + 1][col];
            }
        }

        int result = -2147483648;
        for (int rowUpper = 0; rowUpper < matrix.size(); rowUpper++) {
            for (int colLeft = 0; colLeft < matrix[0].size(); colLeft++) {
                for (int rowLower = rowUpper; rowLower < matrix.size(); rowLower++) {
                    for (int colRight = colLeft; colRight < matrix[0].size(); colRight++) {
                        int currentSum = prefixSum[rowLower + 1][colRight + 1] - prefixSum[rowUpper][colRight + 1] - prefixSum[rowLower + 1][colLeft] + prefixSum[rowUpper][colLeft];
                        if (currentSum <= k) {
                            result = max(result, currentSum);
                        }
                    }
                }
            }
        }
        return result;
    }
};