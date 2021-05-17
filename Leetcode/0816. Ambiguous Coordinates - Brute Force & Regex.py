# https://leetcode.com/problems/ambiguous-coordinates/

import re


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        regex = re.compile('(^([1-9]\d*|0)$)|(^([1-9]\d*|0)\.0*[1-9]+(\d*[1-9]+)*$)')

        strNum = s[1:-1]
        result = set()
        for indexComma in range(1, len(strNum)):
            possibleX, possibleY = [], []
            strX, strY = strNum[:indexComma], strNum[indexComma:]
            # Get X possibility
            if regex.match(strX):
                possibleX.append(strX)
            for decimalX in range(1, len(strX)):
                strFX = strX[:decimalX] + "." + strX[decimalX:]
                if regex.match(strFX):
                    possibleX.append(strFX)
            # Get Y possibility
            if regex.match(strY):
                possibleY.append(strY)
            for decimalY in range(1, len(strY)):
                strFY = strY[:decimalY] + "." + strY[decimalY:]
                if regex.match(strFY):
                    possibleY.append(strFY)
            for strX in possibleX:
                for strY in possibleY:
                    temp = "(" + strX + ", " + strY + ")"
                    result.add(temp)

        return list(result)
