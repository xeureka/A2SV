# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            
            if price < min_price:
                min_price = price
            
            else:
                max_profit = max(max_profit,price - min_price)
        
        return max_profit