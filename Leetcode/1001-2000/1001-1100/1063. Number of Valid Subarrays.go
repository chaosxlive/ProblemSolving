// https://leetcode.com/problems/number-of-valid-subarrays/

func validSubarrays(nums []int) int {
	stack := &Stack{}
	result := 0
	for _, v := range nums {
		for stack.Len() > 0 && v < stack.Last() {
			stack.Pop()
		}
		stack.Push(v)
		result += stack.Len()
	}
	return result
}

type Stack struct {
	list []int
}

func (s *Stack) Pop() int {
	if len(s.list) == 0 {
		return -1
	}
	tmp := s.list[len(s.list)-1]
	s.list = s.list[:len(s.list)-1]
	return tmp
}

func (s *Stack) Push(element int) {
	s.list = append(s.list, element)
}

func (s *Stack) Len() int {
	return len(s.list)
}

func (s *Stack) Last() int {
	return s.list[len(s.list)-1]
}
