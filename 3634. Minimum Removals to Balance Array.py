class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        left = bisect_right(nums, nums[0] * k)
        j = len(nums) - 1
        right = bisect_left(nums, nums[j] / k)
        ans = 0
        while nums[i] * k < nums[j]:
            while nums[i] * k >= nums[left]:
                left += 1
            while nums[j] <= nums[right] * k:
                right -= 1
            if left - i <= j - right:
                i += 1
            else:
                j -= 1
            ans += 1
        return ans