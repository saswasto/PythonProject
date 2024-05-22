from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            if grid[i][0] == 0:
                grid[i] = self.toggle_row(grid[i])
        for j in range(1, cols):
            count_ones = sum(grid[i][j] for i in range(rows))
            if count_ones < rows / 2:
                self.toggle_col(grid, j)
        score = sum(int("".join(map(str, row)), 2) for row in grid)
        return score
    def toggle_row(self, row):
        return [1 - num for num in row]
    def toggle_col(self, matrix, col_idx):
        for row in matrix:
            row[col_idx] = 1 - row[col_idx]
