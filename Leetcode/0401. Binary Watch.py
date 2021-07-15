# https://leetcode.com/problems/binary-watch/

from collections import defaultdict


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        numBitCount = [0] * 60
        bias = 1
        biasEnd = 1
        for n in range(1, 60):
            numBitCount[n] = numBitCount[n - bias] + 1
            if n == biasEnd:
                bias <<= 1
                biasEnd = biasEnd * 2 + 1

        bits = defaultdict(list)
        for i in range(60):
            bits[numBitCount[i]].append(i)

        def getTimes(result, bits, hourBit, minuteBit):
            hours, minutes = bits[hourBit], bits[minuteBit]
            if len(hours) == 0 or hours[0] >= 12 or len(minutes) == 0:
                return
            for hour in hours:
                if hour >= 12:
                    break
                for minute in minutes:
                    temp = [str(hour), ":"]
                    if minute < 10:
                        temp.append("0")
                    temp.append(str(minute))
                    result.append("".join(temp))

        result = []
        for h in range(turnedOn + 1):
            getTimes(result, bits, h, turnedOn - h)

        return result
