class Solution:
    """ The key to this one is realizing that they don't require you to store
    the indices of the buy and sell points. As long as you save the max profit,
    you can move the pointers around wherever"""
    
    def maxProfit(self, prices) -> int:
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit



s = Solution()
print(s.maxProfit([1,3,5,7]))

                

            