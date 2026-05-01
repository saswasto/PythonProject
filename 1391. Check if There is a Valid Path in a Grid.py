from typing import List
from collections import deque
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = {
            1: [(0, -1), (0, 1)],     
            2: [(-1, 0), (1, 0)],     
            3: [(0, -1), (1, 0)],     
            4: [(0, 1), (1, 0)],      
            5: [(0, -1), (-1, 0)],    
            6: [(0, 1), (-1, 0)]     
        }
        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }
        visited = set()
        queue = deque([(0, 0)])
        visited.add((0, 0))
        while queue:
            x, y = queue.popleft()

            if (x, y) == (m - 1, n - 1):
                return True
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if opposite[(dx, dy)] in dirs[grid[nx][ny]]:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        return False