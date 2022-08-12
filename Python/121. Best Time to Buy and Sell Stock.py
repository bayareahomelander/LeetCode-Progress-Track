class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 # Initializing left pointer
        profit = 0 # Max profit, final return value
        
        for r in range(1, len(prices)):
        
            # If price on the previous day is greater than the next day, move left pointer all the way to where right pointer is.
            if prices[l] > prices[r]:
                l = r
            
            else: # Else, update the current maximum value.
                profit = max(prices[r] - prices[l], profit)
        
        return profit

'''
Time: O(n)
Space: O(n)
'''
