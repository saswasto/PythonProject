from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Initialize the queue with the position of all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If there are no fresh oranges, return 0 immediately
        if fresh_count == 0:
            return 0

        # Possible directions of adjacent cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes_passed = 0

        # BFS to rot adjacent fresh oranges
        while queue and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dr, dc in directions:
                    nx, ny = x + dr, y + dc
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))

        # If there are still fresh oranges left, return -1
        if fresh_count > 0:
            return -1
        return minutes_passed
