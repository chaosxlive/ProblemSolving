// https://leetcode.com/problems/maximum-distance-in-arrays/

static int fast_io = []() {
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int curMax = arrays[0].back();
        int curMin = arrays[0].front();
        int result = 0;
        for (int i = 1; i < arrays.size(); i++) {
            result = max({result, abs(arrays[i].front() - curMax), abs(arrays[i].back() - curMin)});
            curMax = max(curMax, arrays[i].back());
            curMin = min(curMin, arrays[i].front());
        }
        return result;
    }
};