class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # initialize l and r pointer
        l, r = 0, 1

        # initialize max profit variable to be overwritten
        maxP = 0

        # while the right pointer is in the bounds of the prices array, continue
        while r < len(prices):
            if prices[l] < prices[r]:               # if the value at the l pointer is less than the value at the right pointer
                profit = prices[r] - prices[l]      # the profit is going to be the r pointer minus l pointer
                maxP = max(maxP, profit)            # maxP is then set to equal what ever is higher, what was already in maxP or the newly calculated profit
            else:
                l = r       # else set l to r to secure the lowest posible price
            r += 1          # move r plus 1 to the right

        return maxP

