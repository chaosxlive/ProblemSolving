# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        billions = num // 1000000000
        millions = (num // 1000000) % 1000
        thousands = (num // 1000) % 1000
        rest = num % 1000

        result = []

        def getWordUntilThousand(num):
            numWord = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            num10Word = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            result = []
            if num >= 100:
                result.append(numWord[num // 100])
                result.append("Hundred")
                num %= 100
            if num >= 20:
                result.append(num10Word[num // 10])
                num %= 10
            if num > 0:
                result.append(numWord[num])
            return " ".join(result)

        if billions != 0:
            result.append(getWordUntilThousand(billions))
            result.append("Billion")
        if millions != 0:
            result.append(getWordUntilThousand(millions))
            result.append("Million")
        if thousands != 0:
            result.append(getWordUntilThousand(thousands))
            result.append("Thousand")
        if rest != 0:
            result.append(getWordUntilThousand(rest))
        return " ".join(result)
