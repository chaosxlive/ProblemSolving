# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        canFlowToPacific = set()
        walked = set()
        q = deque()
        # Pacific
        for row in range(len(heights)):
            if (row, 0) not in walked:
                q.clear()
                q.append((row, 0))
                walked.add((row, 0))
                while len(q) > 0:
                    r, c = q.popleft()
                    canFlowToPacific.add((r, c))
                    for dr, dc in dirs:
                        if 0 <= r + dr < len(heights) and 0 <= c + dc < len(heights[0]) and heights[r][c] <= heights[r + dr][c + dc] and (r + dr, c + dc) not in walked:
                            walked.add((r + dr, c + dc))
                            q.append((r + dr, c + dc))
        for col in range(len(heights[0])):
            if (0, col) not in walked:
                q.clear()
                q.append((0, col))
                walked.add((0, col))
                while len(q) > 0:
                    r, c = q.popleft()
                    canFlowToPacific.add((r, c))
                    for dr, dc in dirs:
                        if 0 <= r + dr < len(heights) and 0 <= c + dc < len(heights[0]) and heights[r][c] <= heights[r + dr][c + dc] and (r + dr, c + dc) not in walked:
                            walked.add((r + dr, c + dc))
                            q.append((r + dr, c + dc))
        # Atlantic
        walked.clear()
        result = []
        for row in range(len(heights)):
            if (row, len(heights[0]) - 1) not in walked:
                q.clear()
                q.append((row, len(heights[0]) - 1))
                walked.add((row, len(heights[0]) - 1))
                while len(q) > 0:
                    r, c = q.popleft()
                    if (r, c) in canFlowToPacific:
                        result.append([r, c])
                    for dr, dc in dirs:
                        if 0 <= r + dr < len(heights) and 0 <= c + dc < len(heights[0]) and heights[r][c] <= heights[r + dr][c + dc] and (r + dr, c + dc) not in walked:
                            walked.add((r + dr, c + dc))
                            q.append((r + dr, c + dc))
        for col in range(len(heights[0])):
            if (len(heights) - 1, col) not in walked:
                q.clear()
                q.append((len(heights) - 1, col))
                walked.add((len(heights) - 1, col))
                while len(q) > 0:
                    r, c = q.popleft()
                    if (r, c) in canFlowToPacific:
                        result.append([r, c])
                    for dr, dc in dirs:
                        if 0 <= r + dr < len(heights) and 0 <= c + dc < len(heights[0]) and heights[r][c] <= heights[r + dr][c + dc] and (r + dr, c + dc) not in walked:
                            walked.add((r + dr, c + dc))
                            q.append((r + dr, c + dc))
        return result
