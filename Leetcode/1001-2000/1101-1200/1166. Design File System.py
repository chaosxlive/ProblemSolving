# https://leetcode.com/problems/design-file-system/

class FileSystem:

    def __init__(self):
        self.fs = {
            'value': 0,
            'children': {},
        }

    def createPath(self, path: str, value: int) -> bool:
        ps = path.split('/')
        i = 1
        p = self.fs
        while i < len(ps) - 1:
            if ps[i] not in p['children']:
                return False
            p = p['children'][ps[i]]
            i += 1
        if ps[-1] in p['children']:
            return False
        p['children'][ps[-1]] = {
            'value': value,
            'children': {},
        }
        return True

    def get(self, path: str) -> int:
        ps = path.split('/')
        i = 1
        p = self.fs
        while i < len(ps):
            if ps[i] not in p['children']:
                return -1
            p = p['children'][ps[i]]
            i += 1
        return p['value']


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
