# https://leetcode.com/contest/biweekly-contest-52/problems/rotating-the-box/

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        boxCount = [[0 for col in range(len(box[0]))] for row in range(len(box))]

        for boxRow in range(len(box)):
            boxCount[boxRow][0] = 1 if box[boxRow][0] == '#' else 0
            for boxCol in range(1, len(box[0])):
                if box[boxRow][boxCol] == '#':
                    boxCount[boxRow][boxCol] = boxCount[boxRow][boxCol - 1] + 1
                elif box[boxRow][boxCol] == '.':
                    boxCount[boxRow][boxCol] = boxCount[boxRow][boxCol - 1]
                else:
                    boxCount[boxRow][boxCol] = 0

        result = [['.' for col in range(len(box))] for row in range(len(box[0]))]
        for boxRow in range(len(box)):
            now = boxCount[boxRow][-1]
            for boxCol in range(len(box[0]) - 1, -1, -1):
                if now == 0:
                    if box[boxRow][boxCol] == '*':
                        result[boxCol][-boxRow - 1] = '*'
                        if boxCol > 0:
                            now = boxCount[boxRow][boxCol - 1]
                    else:
                        if now == 0:
                            result[boxCol][-boxRow - 1] = '.'
                        else:
                            result[boxCol][-boxRow - 1] = '#'
                            now -= 1
                else:
                    result[boxCol][-boxRow - 1] = '#'
                    now -= 1

        return result
