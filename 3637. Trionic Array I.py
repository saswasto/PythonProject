rom typing import List
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        up1 = 0
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
            up1 += 1
        if up1 == 0 or i == n - 1:
            return False
        down = 0
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
            down += 1
        if down == 0 or i == n - 1:
            return False
        up2 = 0
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
            up2 += 1
        return up2 > 0 and i == n - 1
