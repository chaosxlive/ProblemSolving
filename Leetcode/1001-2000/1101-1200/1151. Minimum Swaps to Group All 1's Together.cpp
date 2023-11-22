// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

class Solution {
public:
    int minSwaps(vector<int>& data) {
		int result = data.size();
		int oneCount = 0;
		for (int i = 0; i < data.size(); i++) {
			if (data.at(i) == 1) {
				oneCount++;
			}
		}
		if (oneCount == 0) {
			return 0;
		}
		int windowCount = 0;
		for (int i = 0; i < oneCount - 1; i++) {
			if (data.at(i) == 1) {
				windowCount++;
			}
		}
		for (int i = 0; i < data.size() - oneCount + 1; i++) {
			windowCount += data.at(i + oneCount - 1);
			result = min(result, oneCount - windowCount);
			windowCount -= data.at(i);
		}
		return result;
    }
};