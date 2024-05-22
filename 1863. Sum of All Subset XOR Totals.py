from typing import List
from functools import lru_cache
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, xors: int) -> int:
            if i == len(nums):
                return xors
            include = dfs(i+1, xors ^ nums[i])
            exclude = dfs(i + 1, xors)
            return include + exclude
        return dfs(0,0)
solution = Solution()
print(solution.subsetXORSum([1,3]))
print(solution.subsetXORSum([5, 1, 6]))
print(solution.subsetXORSum([3, 4, 5, 6, 7, 8]))