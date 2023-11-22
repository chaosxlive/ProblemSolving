# https://leetcode.com/problems/design-in-memory-file-system/

class FsNode:

    def __init__(self, isDir: bool, title='', content='') -> None:
        self.isDir = isDir
        self.children = {}
        self.title = title
        self.isFile = not isDir
        self.content = content

    def ls(self):
        return sorted(self.children.keys())

    def getChild(self, dirName):
        if dirName not in self.children:
            self.children[dirName] = FsNode(True)
        return self.children[dirName]


class FileSystem:

    def __init__(self):
        self.root = FsNode(True)

    def ls(self, path: str) -> List[str]:
        d = self.root
        if path == '/':
            return d.ls()
        dirs = path.split('/')
        for i in range(1, len(dirs)):
            d = d.getChild(dirs[i])
        return d.ls() if d.isDir else [d.title]

    def mkdir(self, path: str) -> None:
        d = self.root
        dirs = path.split('/')
        for i in range(1, len(dirs)):
            d = d.getChild(dirs[i])

    def addContentToFile(self, filePath: str, content: str) -> None:
        d = self.root
        dirs = filePath.split('/')
        for i in range(1, len(dirs) - 1):
            d = d.getChild(dirs[i])
        if dirs[-1] not in d.children:
            d.children[dirs[-1]] = FsNode(False, dirs[-1], content)
        else:
            d.children[dirs[-1]].content += content

    def readContentFromFile(self, filePath: str) -> str:
        d = self.root
        dirs = filePath.split('/')
        for i in range(1, len(dirs) - 1):
            d = d.getChild(dirs[i])
        return d.children[dirs[-1]].content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
