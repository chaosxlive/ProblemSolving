# https://leetcode.com/problems/robot-room-cleaner/

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    class Robot:
        def move(self) -> bool:
            """
            Returns true if the cell in front is open and robot moves into the cell.
            Returns false if the cell in front is blocked and robot stays in the current cell.
            :rtype bool
            """

        def turnLeft(self):
            """
            Robot will stay in the same cell after calling turnLeft/turnRight.
            Each turn will be 90 degrees.
            :rtype void
            """

        def turnRight(self):
            """
            Robot will stay in the same cell after calling turnLeft/turnRight.
            Each turn will be 90 degrees.
            :rtype void
            """

        def clean(self):
            """
            Clean the current cell.
            :rtype void
            """

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))


class Solution:
    def cleanRoom(self, robot: 'Robot'):
        checked = set()

        def solve(x: int, y: int, facingDir: int):
            checked.add((x, y))
            robot.clean()
            # Go straight
            di = facingDir
            dx, dy = dirs[di]
            if (x + dx, y + dy) not in checked:
                if not robot.move():
                    checked.add((x + dx, y + dy))
                    robot.turnRight()
                else:
                    solve(x + dx, y + dy, di)
                    robot.turnLeft()
            else:
                robot.turnRight()
            # Go right
            di += 1
            di %= 4
            dx, dy = dirs[di]
            if (x + dx, y + dy) not in checked:
                if not robot.move():
                    checked.add((x + dx, y + dy))
                    robot.turnLeft()
                    robot.turnLeft()
                else:
                    solve(x + dx, y + dy, di)
            else:
                robot.turnLeft()
                robot.turnLeft()
            # Go left
            di -= 2
            di %= 4
            dx, dy = dirs[di]
            if (x + dx, y + dy) not in checked:
                if not robot.move():
                    checked.add((x + dx, y + dy))
                    robot.turnLeft()
                else:
                    solve(x + dx, y + dy, di)
                    robot.turnRight()
            else:
                robot.turnLeft()
            # Go back
            robot.move()
            di -= 1
            di %= 4 
            dx, dy = dirs[di]
            if (x + dx, y + dy) not in checked:
                solve(x + dx, y + dy, di)

        solve(0, 0, 0)
