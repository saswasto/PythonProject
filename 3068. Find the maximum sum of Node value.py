from typing import List
class Solution:
    def maximumValueSum(self,nums: List[int], k: int, edges: List[List[int]])-> int:
        original_sum =0
        xor_sum = 0
        for value in nums:
            original_sum += value
            xor_sum += value^k
        return max(original_sum, xor_sum)
solution = Solution()
nums1 = [1,2,1]
k1 = 3
edges1 = [[0,1], [0,2]]
print(solution.maximumValueSum(nums1, k1, edges1))
nums2 = [2,3]
k2= 7
edges2 = [[0, 1]]
print(solution.maximumValueSum(nums2, k2, edges2))
nums3 = [7,7,7,7,7,7]
k3 = 3
edges3 = [[0,1], [0,2], [0,3], [0,4], [0,5]]
print(solution.maximumValueSum(nums3, k3, edges3))