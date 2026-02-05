class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        res = float("-inf")
        l = p = q = 0
        window_sum = nums[0]

        for r in range(1, n):
            window_sum += nums[r]
            if nums[r - 1] == nums[r]:
                l = p = q = r
                window_sum = nums[r]
                continue
            if nums[r - 1] > nums[r]:
                if r > 1 and nums[r - 2] < nums[r - 1]:
                    p = r - 1
                    while l < q:
                        window_sum -= nums[l]
                        l += 1
                    while l + 1 < p and nums[l] < 0:
                        window_sum -= nums[l]
                        l += 1
            else:
                if r > 1 and nums[r - 2] > nums[r - 1]:
                    q = r - 1
                if l < p < q:
                    res = max(res, window_sum)

        return res