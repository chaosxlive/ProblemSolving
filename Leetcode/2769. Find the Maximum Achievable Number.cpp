// https://leetcode.com/problems/find-the-maximum-achievable-number/

const static auto Init = []{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    int theMaximumAchievableX(int num, int t) {
        return num + t * 2;
    }
};