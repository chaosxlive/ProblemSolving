# https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
                  'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        days, month, year = date.split(' ')
        return year + "-" + months[month] + "-" + ("" if int(days[:-2]) >= 10 else "0") + days[:-2]
