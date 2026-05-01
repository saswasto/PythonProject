class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = 0
        m, n = len(nums1), len(nums2)

        for i in range(m):
            lo, hi = i, n - 1

            while lo <= hi:
                mid = (lo + hi) // 2

                if nums2[mid] >= nums1[i]:
                    max_dist = max(max_dist, mid - i)
                    lo = mid + 1
                else:
                    hi = mid - 1

        return max_dist