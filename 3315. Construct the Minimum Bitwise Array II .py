# 3315. Construct the Minimum Bitwise Array II

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue
            k = 0
            temp = p
            while temp & 1:
                k += 1
                temp >>= 1
            ans.append(p - (1 << (k - 1)))
        
        return ans