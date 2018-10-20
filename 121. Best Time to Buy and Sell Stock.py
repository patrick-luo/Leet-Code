class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        profit = 0
        lowest = prices[0]
        for pi in prices[1:]:
            if pi < lowest:
                lowest = pi
            else:
                profit = max(profit, pi-lowest)
        return profit
