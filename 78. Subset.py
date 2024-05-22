from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        pow_set_size = 1 << n
        for i in range(pow_set_size):
            subset = []
            for j in range(n):
                if (i &(1 << j)) != 0:
                    subset.append(nums[j])
            result.append(subset)
        return result

