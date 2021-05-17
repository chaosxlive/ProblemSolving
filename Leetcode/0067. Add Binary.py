# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        indexA, indexB = len(a) - 1, len(b) - 1
        result = []
        while indexA >= 0 and indexB >= 0:
            if carry:
                if a[indexA] == '1':
                    if b[indexB] == '1':
                        result.append('1')
                    else:
                        result.append('0')
                else:
                    if b[indexB] == '1':
                        result.append('0')
                    else:
                        result.append('1')
                        carry = False
            else:
                if a[indexA] == '1':
                    if b[indexB] == '1':
                        result.append('0')
                        carry = True
                    else:
                        result.append('1')
                else:
                    if b[indexB] == '1':
                        result.append('1')
                    else:
                        result.append('0')
            indexA -= 1
            indexB -= 1

        while indexA >= 0:
            if carry:
                if a[indexA] == '1':
                    result.append('0')
                else:
                    result.append('1')
                    carry = False
            else:
                if a[indexA] == '1':
                    result.append('1')
                else:
                    result.append('0')
            indexA -= 1

        while indexB >= 0:
            if carry:
                if b[indexB] == '1':
                    result.append('0')
                else:
                    result.append('1')
                    carry = False
            else:
                if b[indexB] == '1':
                    result.append('1')
                else:
                    result.append('0')
            indexB -= 1

        if carry:
            result.append('1')

        return "".join(result[::-1])
