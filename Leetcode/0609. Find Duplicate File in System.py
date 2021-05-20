# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = {}
        for path in paths:
            filePath, *files = path.split(' ')
            for file in files:
                temp = file.split('(')
                fileName, fileContent = temp[0], temp[1][:-1]
                if fileContent not in contents:
                    contents[fileContent] = []
                contents[fileContent].append(filePath + "/" + fileName)

        result = []
        for content in contents.values():
            if len(content) > 1:
                result.append(content[:])
        return result
