# https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        temp = []
        line = 0
        isMultiLine = False
        while line < len(source):
            index = 0
            while index < len(source[line]):
                if source[line][index:index + 2] == '//' and not isMultiLine:
                    if len(temp) > 0:
                        result.append("".join(temp))
                        temp.clear()
                    break
                elif source[line][index:index + 2] == '/*' and not isMultiLine:
                    isMultiLine = True
                    index += 1
                elif source[line][index:index + 2] == '*/' and isMultiLine:
                    isMultiLine = False
                    index += 1
                elif not isMultiLine:
                    temp.append(source[line][index])

                index += 1
            if len(temp) > 0 and not isMultiLine:
                result.append("".join(temp))
                temp.clear()
            line += 1
        return result
