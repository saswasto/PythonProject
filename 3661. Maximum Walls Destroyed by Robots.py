class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)

        x = [[robots[i], distance[i]] for i in range(n)]

        x.sort()
        walls.sort()

        x.append([10**9, 0])

        def query(l, r):
            if l > r:
                return 0
            return bisect.bisect_right(walls, r) - bisect.bisect_left(walls, l)

        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = query(x[0][0] - x[0][1], x[0][0])

        if n > 1:
            dp[0][1] = query(
                x[0][0],
                min(x[1][0] - 1, x[0][0] + x[0][1])
            )
        else:
            dp[0][1] = query(x[0][0], x[0][0] + x[0][1])

        for i in range(1, n):

            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + \
                       query(
                           x[i][0],
                           min(x[i + 1][0] - 1, x[i][0] + x[i][1])
                       )

            dp[i][0] = dp[i - 1][0] + \
                       query(
                           max(x[i][0] - x[i][1], x[i - 1][0] + 1),
                           x[i][0]
                       )

            leftStart = max(x[i][0] - x[i][1], x[i - 1][0] + 1)
            leftEnd = x[i][0]

            overlapStart = leftStart
            overlapEnd = min(x[i - 1][0] + x[i - 1][1], x[i][0] - 1)

            res = dp[i - 1][1] + \
                  query(leftStart, leftEnd) - \
                  query(overlapStart, overlapEnd)

            dp[i][0] = max(dp[i][0], res)

        return max(dp[n - 1][0], dp[n - 1][1])