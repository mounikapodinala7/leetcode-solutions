class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]

        for i in range(n - 2, -1, -1):
            for j in range(i, -1, -1):
                down = triangle[i][j] + dp[i + 1][j]
                downRight = triangle[i][j] + dp[i + 1][j + 1]
                dp[i][j] = min(down, downRight)

        return dp[0][0]