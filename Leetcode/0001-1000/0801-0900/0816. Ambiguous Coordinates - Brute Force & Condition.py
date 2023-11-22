# https://leetcode.com/problems/ambiguous-coordinates/

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def checkCoordinatValid(coord, isDecimalPoint=True):
            if isDecimalPoint:
                return (coord[0] != '0' or coord[1] == '.') and coord[-1] != '0'
            try:
                return (int(coord) > 0 and coord[0] != '0') or len(coord) == 1
            except:
                return False
            

        strNum = s[1:-1]
        result = set()
        for indexComma in range(1, len(strNum)):
            possibleX, possibleY = [], []
            strX, strY = strNum[:indexComma], strNum[indexComma:]
            # Get X possibility
            if checkCoordinatValid(strX, False):
                possibleX.append(strX)
            for decimalX in range(1, len(strX)):
                strFX = strX[:decimalX] + "." + strX[decimalX:]
                if checkCoordinatValid(strFX):
                    possibleX.append(strFX)
            # Get Y possibility
            if checkCoordinatValid(strY, False):
                possibleY.append(strY)
            for decimalY in range(1, len(strY)):
                strFY = strY[:decimalY] + "." + strY[decimalY:]
                if checkCoordinatValid(strFY):
                    possibleY.append(strFY)
            for strX in possibleX:
                for strY in possibleY:
                    temp = "(" + strX + ", " + strY + ")"
                    result.add(temp)

        return list(result)
