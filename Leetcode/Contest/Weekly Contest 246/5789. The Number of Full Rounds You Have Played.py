# https://leetcode.com/contest/weekly-contest-246/problems/the-number-of-full-rounds-you-have-played/

class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        hourStart, minuteStart = int(startTime[:2]), int(startTime[3:])
        hourFinish, minuteFinish = int(finishTime[:2]), int(finishTime[3:])
        if hourFinish < hourStart or (hourFinish == hourStart and minuteFinish < minuteStart):
            hourFinish += 24

        if minuteStart == 0:
            minuteStart = 0
        elif 0 < minuteStart <= 15:
            minuteStart = 15
        elif 15 < minuteStart <= 30:
            minuteStart = 30
        elif 30 < minuteStart <= 45:
            minuteStart = 45
        else:
            hourStart += 1
            minuteStart = 0
            
        if 0 <= minuteFinish < 15:
            minuteFinish = 0
        elif 15 <= minuteFinish < 30:
            minuteFinish = 15
        elif 30 <= minuteFinish < 45:
            minuteFinish = 30
        else:
            minuteFinish = 45

        return (hourFinish - hourStart) * 4 + (minuteFinish - minuteStart) // 15
