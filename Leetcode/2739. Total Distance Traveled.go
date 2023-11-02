// https://leetcode.com/problems/total-distance-traveled/

func distanceTraveled(mainTank int, additionalTank int) int {
    result := 0
    for mainTank >= 5 && additionalTank > 0 {
        transfered := min(int(mainTank / 5), additionalTank)
        result += 50 * transfered
        mainTank -= 4 * transfered
        additionalTank -= transfered
    }
    return result + mainTank * 10
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}