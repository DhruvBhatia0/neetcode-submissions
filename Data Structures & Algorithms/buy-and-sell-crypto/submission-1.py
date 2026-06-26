class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0
        
        buy = 0
        sell = 1

        max_profit = 0

        while True:
            buy_price, sell_price = prices[buy], prices[sell]

            profit = sell_price - buy_price

            max_profit = max(profit, max_profit)

            if buy_price > sell_price:
                buy = sell
            sell += 1
            
            if sell == len(prices):
                break
        
        return max_profit