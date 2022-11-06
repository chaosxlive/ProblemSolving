# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        result = ['']
        for d in filter(lambda x: len(x) > 0, path.split('/')):
            if d == '.':
                continue
            if d == '..':
                if len(result) > 1:
                    result.pop()
                continue
            else:
                result.append(d)
        return '/'.join(result) if len(result) > 1 else '/'
