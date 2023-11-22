# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [[]]
        linesSpaceRest = [maxWidth]
        currentLineLength = 0
        for word in words:
            if currentLineLength == 0:
                lines[-1].append(word)
                linesSpaceRest[-1] -= len(word)
                currentLineLength += len(word)
            elif len(word) + 1 + currentLineLength > maxWidth:
                lines.append([word])
                linesSpaceRest.append(maxWidth - len(word))
                currentLineLength = len(word)
            else:
                lines[-1].append(word)
                linesSpaceRest[-1] -= len(word)
                currentLineLength += len(word) + 1
        result = []
        for lineIdx in range(len(lines) - 1):
            line = lines[lineIdx]
            spaceCnt = linesSpaceRest[lineIdx]
            if len(line) == 1:
                result.append(line[0] + ' ' * spaceCnt)
            else:
                tempLine = []
                thresholdIdx = spaceCnt % (len(line) - 1)
                gapSpaceCnt = spaceCnt // (len(line) - 1)
                for i in range(len(line) - 1):
                    tempLine.append(line[i])
                    tempLine.append(' ' * (gapSpaceCnt + 1) if i < thresholdIdx else ' ' * gapSpaceCnt)
                tempLine.append(line[-1])
                result.append(''.join(tempLine))
        result.append(' '.join(lines[-1]) + ' ' * (linesSpaceRest[-1] - (len(lines[-1]) - 1)))
        return result
