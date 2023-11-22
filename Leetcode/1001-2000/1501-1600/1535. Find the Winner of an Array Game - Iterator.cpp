// https://leetcode.com/problems/find-the-winner-of-an-array-game/

const static auto Init = []{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        if (k == 1) {
            return max(arr[0], arr[1]);
        }
        int a = arr[0];
        int winCnt = 0;
        for (int i = 1; i < arr.size(); i++) {
            int b = arr[i];
            if (a > b) {
                winCnt++;
                if (winCnt == k) {
                    return a;
                }
            } else {
                a = b;
                winCnt = 1;
            }
        }
        return *max_element(arr.begin(), arr.end());
    }
};