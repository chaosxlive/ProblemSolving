# https://leetcode.com/problems/strong-password-checker/

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        lowercaseSet = set('qwertyuiopasdfghjklzxcvbnm')
        uppercaseSet = set('QWERTYUIOPASDFGHJKLZXCVBNM')
        digitSet = set('0123456789')

        hasLowercase = any(c in lowercaseSet for c in password)
        hasUppercase = any(c in uppercaseSet for c in password)
        hasDigit = any(c in digitSet for c in password)

        cntMissingType = 0 + (0 if hasLowercase else 1) + (0 if hasUppercase else 1) + (0 if hasDigit else 1)

        groupLens = [1]
        for i in range(1, len(password)):
            if password[i] == password[i - 1]:
                groupLens[-1] += 1
            else:
                groupLens.append(1)

        delCnt = max(0, len(password) - 20)
        addCnt = max(0, 6 - len(password))
        result = delCnt

        while delCnt > 0:
            groupPick = 0
            while groupPick < len(groupLens) and groupLens[groupPick] < 3:
                groupPick += 1
            if groupPick == len(groupLens):
                groupPick = 0
                while groupLens[groupPick] == 0:
                    groupPick += 1
            for i in range(groupPick + 1, len(groupLens)):
                if groupLens[i] >= 3 and groupLens[i] % 3 < groupLens[groupPick] % 3:
                    groupPick = i
            groupLens[groupPick] -= 1
            delCnt -= 1

        breakGroupCnt = sum(groupLen // 3 for groupLen in groupLens)

        result += max(cntMissingType, breakGroupCnt, addCnt)

        return result
