# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sumEven = 0
        for num in A:
            if num % 2 == 0:
                sumEven += num
        
        result = []
        for query in queries:
            if A[query[1]] % 2 == 0:
                sumEven -= A[query[1]]
            if (A[query[1]] + query[0]) % 2 == 0:
                sumEven += A[query[1]] + query[0]
            A[query[1]] += query[0]
            result.append(sumEven)
        return result
