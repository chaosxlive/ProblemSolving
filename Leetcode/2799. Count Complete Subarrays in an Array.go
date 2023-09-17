func countCompleteSubarrays(nums []int) int {
    result := 0
    distincts := map[int]bool{}
    for _, num := range nums {
        if _, exist := distincts[num]; !exist {
            distincts[num] = true;
        }
    }
    totalDistincts := len(distincts)
    for start := 0; start < len(nums); start++ {
        distinct := map[int]bool{}
        for i := start; i < len(nums); i++ {
            if _, exist := distinct[nums[i]]; !exist {
                distinct[nums[i]] = true
            }
            if len(distinct) == totalDistincts{
                result++
            }
        }
    }
    return result
}