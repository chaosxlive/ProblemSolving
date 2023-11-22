// https://leetcode.com/problems/total-distance-traveled/

function distanceTraveled(mainTank: number, additionalTank: number): number {
    let result = 0;
    while (mainTank >= 5 && additionalTank > 0) {
        let transfered = Math.min(Math.floor(mainTank / 5), additionalTank);
        result += 50 * transfered;
        mainTank -= 4 * transfered;
        additionalTank -= transfered;
    }
    return result + mainTank * 10;
};