# https://leetcode.com/problems/design-sql/

from typing import List


class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.table = {}
        self.pk = {}
        for name in names:
            self.table[name] = {}
            self.pk[name] = 1

    def insertRow(self, name: str, row: List[str]) -> None:
        self.table[name][self.pk[name]] = row
        self.pk[name] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        self.table[name].pop(rowId)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.table[name][rowId][columnId - 1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)
