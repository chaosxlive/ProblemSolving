// https://leetcode.com/problems/find-the-maximum-achievable-number/

class Solution {
    fun theMaximumAchievableX(num: Int, t: Int): Int {
        return num + (t shl 1)
    }
}