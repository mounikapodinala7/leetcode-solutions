class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        cool = 0
        for i in range(1,len(prices)):
            curr_hold = max(cool-prices[i], hold) 
            curr_sold = hold + prices[i]
            curr_cool = max(cool, sold)
            hold, sold, cool = curr_hold, curr_sold, curr_cool
        return max(sold, cool)
