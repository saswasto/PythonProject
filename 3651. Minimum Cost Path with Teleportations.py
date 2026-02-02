class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[grid[i][j]].append((i, j))
        inf = float('inf')
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = 0
        def update():
            for i in range(m):
                for j in range(n):
                    temp = grid[i][j] + min(
                        dp[i-1][j] if i else inf, 
                        dp[i][j-1] if j else inf
                    )
                    if temp < dp[i][j]: dp[i][j] = temp
        update()
        keys = sorted(d, reverse=True)
        for _ in range(k):
            dist = inf
            for key in keys:
                for i, j in d[key]:
                    if dp[i][j] < dist: dist = dp[i][j]
                for i, j in d[key]:
                    dp[i][j] = dist
            update()
        return dp[-1][-1]
        