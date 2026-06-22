class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l=0
        r=1
        max_profit = 0
        while r < n :
            if prices[l] < prices[r]:
                prof = prices[r]-prices[l]
                max_profit = max(max_profit,prof)
            else:
                l=r
            r+=1
        return max_profit
                