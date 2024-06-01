from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Initialize the queue with all rotten oranges and count the fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Directions for the 4 adjacent cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes_passed = 0

        # Perform BFS
        while queue and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dr, dc in directions:
                    nx, ny = x + dr, y + dc

                    # If the adjacent cell is within bounds and is a fresh orange
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        # Make it rotten
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
        if fresh_count > 0:
            return -1
        return minutes_passed

# Example usage:
solution = Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # Output: 4
print(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # Output: -1
print(solution.orangesRotting([[0,2]]))                   # Output: 0
