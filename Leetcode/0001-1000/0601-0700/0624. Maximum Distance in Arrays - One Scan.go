// https://leetcode.com/problems/maximum-distance-in-arrays/

func maxDistance(arrays [][]int) int {
	curMax, curMin, result := float64(arrays[0][len(arrays[0])-1]), float64(arrays[0][0]), float64(0)
	for i := 1; i < len(arrays); i++ {
		fMin, fMax := float64(arrays[i][0]), float64(arrays[i][len(arrays[i])-1])
		result = math.Max(result, math.Abs(fMin-curMax))
		result = math.Max(result, math.Abs(fMax-curMin))
		curMax = math.Max(curMax, fMax)
		curMin = math.Min(curMin, fMin)
	}
	return int(result)
}
