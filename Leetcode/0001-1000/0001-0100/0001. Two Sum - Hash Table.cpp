// https://leetcode.com/problems/two-sum/

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

static auto fast_io = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            unordered_map<int, int>::iterator it = seen.find(target - num);
            if (it != seen.end()) {
                return {it->second, i};
            }
            seen[num] = i;
        }
        return {-1, -1};
    }
};