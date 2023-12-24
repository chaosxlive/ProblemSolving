class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []

        def getPriority(c: str):
            if c == '+' or c == '-':
                return 1
            if c == '/' or c == '*':
                return 2
            return 0

        def calcOp(op: str, n1: int, n2: int):
            if op == '+':
                return n1 + n2
            if op == '-':
                return n1 - n2
            if op == '*':
                return n1 * n2
            if op == '/':
                if n1 < 0 and n2 > 0:
                    return -((-n1) // n2)
                if n1 > 0 and n2 < 0:
                    return -(n1 // (-n2))
                if n1 < 0 and n2 < 0:
                    return (-n1) // (-n2)
                return n1 // n2
            return 0
        temp = 0
        isTempDirty = False
        for c in s:
            if '0' <= c <= '9':
                temp = temp * 10 + int(c)
                isTempDirty = True
            elif c == '(':
                ops.append(c)
            elif c == ')':
                if isTempDirty:
                    nums.append(temp)
                    temp = 0
                    isTempDirty = False
                while ops[-1] != '(':
                    nums[-2] = calcOp(ops[-1], nums[-2], nums[-1])
                    ops.pop()
                    nums.pop()
                ops.pop()
            else:
                if isTempDirty:
                    nums.append(temp)
                    temp = 0
                    isTempDirty = False
                if len(ops):
                    while len(ops) and getPriority(c) <= getPriority(ops[-1]):
                        nums[-2] = calcOp(ops[-1], nums[-2], nums[-1])
                        ops.pop()
                        nums.pop()
                ops.append(c)

        if isTempDirty:
            nums.append(temp)

        while len(ops):
            nums[-2] = calcOp(ops[-1], nums[-2], nums[-1])
            ops.pop()
            nums.pop()

        return nums[-1]
