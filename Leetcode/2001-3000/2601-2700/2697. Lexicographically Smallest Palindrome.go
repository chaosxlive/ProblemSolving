// https://leetcode.com/problems/lexicographically-smallest-palindrome/

package leetcode

import (
	"strings"
)

func makeSmallestPalindrome(s string) string {
	temp := strings.Split(s, "")
	l := len(s)
	for i := 0; i < l/2; i++ {
		if temp[i] != temp[l-i-1] {
			if temp[i] < temp[l-i-1] {
				temp[l-i-1] = temp[i]
			} else {
				temp[i] = temp[l-i-1]
			}
		}
	}
	return strings.Join(temp, "")
}
