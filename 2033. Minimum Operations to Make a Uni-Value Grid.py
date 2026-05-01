class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = [num for row in grid for num in row]

        remainder = values[0] % x
        for num in values:
            if num % x != remainder:
                return -1 

        values.sort()
        median = values[len(values) // 2]

        return sum(abs(num - median) // x for num in values)  