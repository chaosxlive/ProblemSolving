func maximumSubarraySum(nums []int, k int) int64 {
	prefix := make([]int, len(nums)+1)
	idxMap := map[int][]int{}
	for i, v := range nums {
		prefix[i+1] = prefix[i] + v
		if _, exist := idxMap[v]; !exist {
			idxMap[v] = []int{}
		}
		idxMap[v] = append(idxMap[v], i)
	}
	var result int64
	result = -9223372036854775808
	for i, n := range nums {
		if idxs, exist := idxMap[n-k]; exist {
			for _, j := range idxs {
				if j < i {
					continue
				}
				result = max(result, int64(prefix[j+1]-prefix[i]))
			}
		}
		if idxs, exist := idxMap[n+k]; exist {
			for _, j := range idxs {
				if j < i {
					continue
				}
				result = max(result, int64(prefix[j+1]-prefix[i]))
			}
		}
	}
	if result == -9223372036854775808 {
		return 0
	}
	return result
}