from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if (
                    row < 0
                    or row >= len(grid)
                    or col < 0
                    or col >= len(grid[0])
                    or grid[row][col] == 0
            ):
                return 0
            gold = grid[row][col]
            original = gold
            grid[row][col] = 0

            gold += max(
                dfs(row + dr, col + dc)
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            )
            grid[row][col] = original
            return gold
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold
# 1st Example:
solution = Solution()
grid = [
    [0, 6, 0],
    [5, 8, 7],
    [0, 9, 0]
]
print(solution.getMaximumGold(grid))  # for the 1st test case the Output should be 24