# https://leetcode.com/problems/prison-cells-after-n-days/

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:

        n %= 14
        if n == 0:
            n = 14

        def change(cells):
            a, b, c, d, e, f, g, h = cells[0], cells[1], cells[2], cells[3], cells[4], cells[5], cells[6], cells[7]
            cells[0] = cells[7] = 0
            cells[1] = not (a ^ c)
            cells[2] = not (b ^ d)
            cells[3] = not (c ^ e)
            cells[4] = not (d ^ f)
            cells[5] = not (e ^ g)
            cells[6] = not (f ^ h)

        for i in range(n):
            change(cells)

        for i in range(8):
            cells[i] = 1 if cells[i] else 0

        return cells
