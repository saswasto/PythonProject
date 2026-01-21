# 3314. Construct the Minimum Bitwise Array I

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for x in nums:
            if x % 2 == 0:
                ans.append(-1)
                continue
            k = 0
            temp = x
            while temp & 1:
                k += 1
                temp >>= 1

            ans.append(x - (1 << (k - 1)))

        return ans
