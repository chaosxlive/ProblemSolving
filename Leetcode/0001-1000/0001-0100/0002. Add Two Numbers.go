package leetcode

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	resultHead := new(ListNode)
	resultPtr := resultHead
	rest := 0
	i1, i2 := l1, l2
	for i1 != nil && i2 != nil {
		newNode := new(ListNode)
		rest = i1.Val + i2.Val + rest
		newNode.Val = rest % 10
		rest /= 10
		resultPtr.Next = newNode
		resultPtr = newNode
		i1, i2 = i1.Next, i2.Next
	}
	for i1 != nil {
		newNode := new(ListNode)
		rest = i1.Val + rest
		newNode.Val = rest % 10
		rest /= 10
		resultPtr.Next = newNode
		resultPtr = newNode
		i1 = i1.Next
	}
	for i2 != nil {
		newNode := new(ListNode)
		rest = i2.Val + rest
		newNode.Val = rest % 10
		rest /= 10
		resultPtr.Next = newNode
		resultPtr = newNode
		i2 = i2.Next
	}
	if rest != 0 {
		newNode := new(ListNode)
		newNode.Val = rest
		resultPtr.Next = newNode
	}

	return resultHead.Next
}
