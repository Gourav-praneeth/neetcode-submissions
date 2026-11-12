class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # optimal solution
        minPrice = prices[0]
        profit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            currentProfit = price - minPrice
            profit = max(currentProfit,profit)
        return profit
            

        
        # Brute Force
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > profit:
        #             profit = prices[j] - prices[i]
        # return profit