# https://leetcode.com/problems/brace-expansion-ii/

from functools import reduce


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def grammerParse(exp, start):
            buffer = [[]]
            index = start

            while index < len(exp):
                if exp[index] == '{':
                    returnList, returnIndex = grammerParse(exp, index + 1)
                    buffer[-1].append(returnList)
                    index = returnIndex + 1
                elif exp[index] == '}':
                    break
                elif exp[index] == ',':
                    buffer.append([])
                    index += 1
                else:
                    buffer[-1].append(exp[index])
                    index += 1

            result = set()
            for picked in buffer:
                result.update(reduce(lambda list1, list2: [str1 + str2 for str2 in list2 for str1 in list1], picked))

            return list(result), index

        result, final = grammerParse(expression, 0)
        result.sort()
        return result
