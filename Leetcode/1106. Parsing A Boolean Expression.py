# https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def parser(exp, index):
            if exp[index] == 't':
                return True, index
            elif exp[index] == 'f':
                return False, index

            params = []
            start = index + 2
            end = start
            while exp[end] != ')':
                if exp[end] == 't':
                    params.append(True)
                elif exp[end] == 'f':
                    params.append(False)
                elif exp[end] != ',':
                    result, end = parser(exp, end)
                    params.append(result)
                end += 1
            if exp[index] == '&':
                return params.count(False) == 0, end
            elif exp[index] == '|':
                return params.count(True) > 0, end
            else:
                return not params[0], end

        result, index = parser(expression, 0)
        return result
