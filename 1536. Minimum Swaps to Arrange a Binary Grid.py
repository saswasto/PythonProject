def trailingZeroes(row: list[int]) -> int:
    try:
        return row[::-1].index(1)
    except ValueError:
        return len(row)

def findMatchIdx(rows: list[int], zeroesNeeded: int) -> int:
    for i, zeroes in enumerate(rows):
        if zeroes >= zeroesNeeded:
            return i
    
    return -1

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        swaps = 0
        rows = [trailingZeroes(row) for row in grid]
        for zeroesNeeded in range(len(rows))[::-1]:
            matchIdx = findMatchIdx(rows, zeroesNeeded)
            if matchIdx < 0: return -1

            swaps += matchIdx
            del rows[matchIdx]
        
        return swaps