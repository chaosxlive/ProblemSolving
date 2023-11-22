# https://leetcode.com/problems/solve-the-equation/

import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        eqLeft, eqRight = equation.split('=')
        componentLeft, componentRight = re.findall('[\+\-]?\d*x?', eqLeft)[:-1], re.findall('[\+\-\*\/]?\d*x?', eqRight)[:-1]
        x = n = 0
        for index in range(len(componentLeft)):
            if componentLeft[index][-1] == 'x':
                if len(componentLeft[index]) == 1:
                    x += 1
                elif len(componentLeft[index]) == 2 and componentLeft[index][0] == '+':
                    x += 1
                elif len(componentLeft[index]) == 2 and componentLeft[index][0] == '-':
                    x -= 1
                else:
                    x += int(componentLeft[index][:-1])
            else:
                n -= int(componentLeft[index])
        for index in range(len(componentRight)):
            if componentRight[index][-1] == 'x':
                if len(componentRight[index]) == 1:
                    x -= 1
                elif len(componentRight[index]) == 2 and componentRight[index][0] == '+':
                    x -= 1
                elif len(componentRight[index]) == 2 and componentRight[index][0] == '-':
                    x += 1
                else:
                    x -= int(componentRight[index][:-1])
            else:
                n += int(componentRight[index])
        if x != 0:
            return "x=" + str(n // x)
        else:
            if n == 0:
                return "Infinite solutions"
            else:
                return "No solution"
