class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        max_dist = 0
        for i in range(n):
            if colors[i] != colors[0]:
                max_dist = i

        for i in range(n - 1, -1, -1):
            if colors[i] != colors[-1]:
                max_dist = max(max_dist, n - 1 - i)
        return max_dist