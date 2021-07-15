# https://leetcode.com/problems/expression-add-operators/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def dfs(result, num, target, buffer, index, isLeadingZero):
            if index == len(num):
                value = "".join(buffer)
                if eval(value) == target:
                    result.append(value)
                return

            buffer.append("")
            buffer.append(num[index])

            if not isLeadingZero:
                dfs(result, num, target, buffer, index + 1, False)

            buffer[-2] = "+"
            dfs(result, num, target, buffer, index + 1, True if num[index] == '0' else False)

            buffer[-2] = "-"
            dfs(result, num, target, buffer, index + 1, True if num[index] == '0' else False)

            buffer[-2] = "*"
            dfs(result, num, target, buffer, index + 1, True if num[index] == '0' else False)

            buffer.pop()
            buffer.pop()

        dfs(result, num, target, [num[0]], 1, True if num[0] == '0' else False)

        return result
