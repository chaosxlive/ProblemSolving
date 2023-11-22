// https://leetcode.com/problems/semi-ordered-permutation/

func semiOrderedPermutation(nums []int) int {
    f, l := -1, -1
    for i, n := range nums {
        if n == 1 {
            f = i
        } else if n == len(nums) {
            l = i
        }
    }
    if f > l {
        return f + len(nums) - l - 2
    }
    return f + len(nums) - l - 1
}