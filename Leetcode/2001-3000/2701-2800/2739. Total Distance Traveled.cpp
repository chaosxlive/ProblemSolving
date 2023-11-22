// https://leetcode.com/problems/total-distance-traveled/

class Solution {
public:
    int distanceTraveled(int mainTank, int additionalTank) {
        int result = 0;
        while (mainTank >= 5 && additionalTank > 0) {
            int transfered = min(int(mainTank / 5), additionalTank);
            result += 50 * transfered;
            mainTank -= 4 * transfered;
            additionalTank -= transfered;
        }
        return result + mainTank * 10;
    }
};