class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        size = m * n
        idx = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        idx.sort(reverse=True)
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0
        for i in range(m):
            for j in range(n):
                if i:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                if j:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])
        for _ in range(k):
            tele = [[float('inf')] * n for _ in range(m)]
            tmin = float('inf')
            p = 0
            while p < size:
                q, v = p, idx[p][0]
                while q < size and idx[q][0] == v:
                    x, i, j = idx[q]
                    tmin = min(tmin, dp[i][j])
                    q += 1
                for r in range(p, q):
                    _, i, j = idx[r]
                    tele[i][j] = tmin
                p = q
            ndp = [row[:] for row in tele]
            for i in range(m):
                for j in range(n):
                    if i:
                        ndp[i][j] = min(ndp[i][j], ndp[i - 1][j] + grid[i][j])
                    if j:
                        ndp[i][j] = min(ndp[i][j], ndp[i][j - 1] + grid[i][j])
            dp = ndp
        return dp[m - 1][n - 1]