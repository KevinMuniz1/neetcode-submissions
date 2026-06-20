## we have an integer array prices where each num is a price of a stock on that day

## we can choose one day to buy a stock and one day to sell 

## we want the best day to buy and sell for max profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0 

        r = 1

        maxProfit = 0 

        while r < len(prices):

            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
            
            else:
                l = r
                r += 1
        

        return maxProfit





        