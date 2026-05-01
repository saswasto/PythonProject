from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        for indices in pos.values():
            k = len(indices)
            
            prefix = [0] * (k + 1)
            for i in range(k):
                prefix[i + 1] = prefix[i] + indices[i]
            
            for i in range(k):
                idx = indices[i]
                
                left = idx * i - prefix[i]
                
                right = (prefix[k] - prefix[i + 1]) - idx * (k - i - 1)
                
                res[idx] = left + right
        
        return res