# https://leetcode.com/problems/parse-lisp-expression/

class Solution:
    def evaluate(self, expression: str) -> int:
        self.variables = {}

        # Parse Operator
        def expParser(expression) -> int:
            if expression[0] == '(':
                exp = expSplitter(expression)
            else:
                return self.variables[expression][-1] if expression in self.variables and len(self.variables[expression]) > 0 else int(expression)

            if exp[1] == 'let':
                return evalLetExp(exp)
            elif exp[1] == 'add':
                return evalAddExp(exp)
            elif exp[1] == 'mult':
                return evalMultExp(exp)

        # Split Expression to Syntax List
        def expSplitter(expression) -> list:
            result = ['(']
            countParentheses = 0
            startIndex = 1
            for index in range(4, len(expression)):
                if expression[index] == '(':
                    countParentheses += 1
                elif expression[index] == ' ' and countParentheses == 0:
                    result.append(expression[startIndex:index])
                    startIndex = index + 1
                elif expression[index] == ')':
                    countParentheses -= 1
            result.append(expression[startIndex:-1])
            result.append(')')
            return result

        def evalLetExp(expression) -> int:
            # Push Variable Definition
            for index in range(2, len(expression) - 3, 2):
                if expression[index] not in self.variables:
                    self.variables[expression[index]] = []
                self.variables[expression[index]].append(expParser(expression[index + 1]))

            result = expParser(expression[-2])

            # Pop Variable Definition
            for index in range(2, len(expression) - 3, 2):
                self.variables[expression[index]].pop()

            return result

        def evalAddExp(expression) -> int:
            param1 = expParser(expression[2])
            param2 = expParser(expression[3])
            return param1 + param2

        def evalMultExp(expression) -> str:
            param1 = expParser(expression[2])
            param2 = expParser(expression[3])
            return param1 * param2

        return expParser(expression)
