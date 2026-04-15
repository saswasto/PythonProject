from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = float('inf')
        
        for i in range(len(nums)):
            if nums[i] == target:
                min_dist = min(min_dist, abs(i - start))
        
        return min_dist