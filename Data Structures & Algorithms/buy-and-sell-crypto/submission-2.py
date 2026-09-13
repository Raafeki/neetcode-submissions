class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        
        most_profit = 0

        buy = 0

        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            profit = prices[sell] - prices[buy]

            most_profit = max(most_profit, profit)

        return most_profit