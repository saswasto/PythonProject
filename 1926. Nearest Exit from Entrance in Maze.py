from collections import deque
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y, steps = queue.popleft()
            for dr, dc in directions:
                nx, ny = x + dr, y + dc
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if maze[nx][ny] == '.':
                        if nx == 0 or ny == 0 or nx == rows - 1 or ny == cols - 1:
                            return steps + 1
                        visited.add((nx, ny))
                        queue.append((nx, ny, steps + 1))
        return -1
# Example usage:
solution = Solution()
print(solution.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))  # Output: 1
print(solution.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]))  # Output: 2
print(solution.nearestExit([[".","+"]], [0,0]))  # Output: -1
