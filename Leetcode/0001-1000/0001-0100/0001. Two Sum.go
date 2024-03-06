// https://leetcode.com/problems/two-sum/

package leetcode

func twoSum(nums []int, target int) []int {
	seen := map[int]int{}
	for i, v := range nums {
		if _, ok := seen[target-v]; ok {
			return []int{seen[target-v], i}
		}
		seen[v] = i
	}
	return []int{-1, -1}
}
