# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices):
        stack = []
        result = [0] * len(prices)
        index = len(prices) - 1
        while index >= 0:
            if len(stack) == 0:
                result[index] = prices[index]
                stack.append(prices[index])
            else:
                if prices[index] >= stack[-1]:
                    result[index] = prices[index] - stack[-1]
                    if prices[index] != stack[-1]:
                        stack.append(prices[index])
                else:
                    while len(stack) != 0 and stack[-1] > prices[index] :
                        stack.pop()
                    if len(stack) == 0:
                        result[index] = prices[index]
                        stack.append(prices[index])
                    else:
                        result[index] = prices[index] - stack[-1]
                        if prices[index] != stack[-1]:
                            stack.append(prices[index])

            index -= 1
        return result
                


test = Solution()
print(test.finalPrices([8, 7, 4, 2, 8, 1, 7, 7, 10, 1]))
