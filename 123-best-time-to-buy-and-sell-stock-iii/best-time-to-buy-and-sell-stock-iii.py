class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n)]

        def find(ind, buy, cap):
            # Base cases
            if ind == n:
                return 0
            if cap == 0:
                return 0

            # Return memoized result
            if dp[ind][buy][cap] != -1:
                return dp[ind][buy][cap]

            if buy == 1:  # Can buy
                take = -prices[ind] + find(ind+1, 0, cap)
                not_take = find(ind+1, 1, cap)
                dp[ind][buy][cap] = max(take, not_take)
            else:  # Must sell
                sell = prices[ind] + find(ind+1, 1, cap-1)
                skip = find(ind+1, 0, cap)
                dp[ind][buy][cap] = max(sell, skip)

            return dp[ind][buy][cap]

        return find(0, 1, 2)