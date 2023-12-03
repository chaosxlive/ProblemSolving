# https://leetcode.com/problems/design-snake-game/

from collections import deque
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.w = width
        self.h = height
        self.food = deque(food)
        self.snake = deque([(0, 0)])
        self.bodyMap = set([(0, 0)])
        self.isGameRunning = True
        self.score = 0

    def move(self, direction: str) -> int:
        if not self.isGameRunning:
            return -1
        headX, headY = self.snake[-1]
        if direction == 'U':
            headY -= 1
        elif direction == 'D':
            headY += 1
        elif direction == 'L':
            headX -= 1
        else:
            headX += 1
        if not (0 <= headX < self.w and 0 <= headY < self.h):
            self.isGameRunning = False
            return -1
        if len(self.food) > 0 and headY == self.food[0][0] and headX == self.food[0][1]:
            self.food.popleft()
            self.score += 1
        else:
            tailX, tailY = self.snake.popleft()
            self.bodyMap.remove((tailX, tailY))
        if (headX, headY) in self.bodyMap:
            self.isGameRunning = False
            return -1
        self.snake.append((headX, headY))
        self.bodyMap.add((headX, headY))
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
