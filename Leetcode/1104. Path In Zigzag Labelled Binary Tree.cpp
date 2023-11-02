// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        vector<int> result = { label };
        while (true) {
            label >>= 1;
            if (label < 1) break;

            int level = floor(log2(label)) + 1;
            int end = pow(2, level);
            int start = end / 2;
            label = end - 1 - label + start;
            result.push_back(label);
        }
        reverse(result.begin(), result.end());
        return result;
    }
};