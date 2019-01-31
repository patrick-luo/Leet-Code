class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [sys.float_info.max]*amount
        for i in xrange(1, amount+1):
            for val in coins:
                if val <= i:
                    dp[i] = min(dp[i], 1+dp[i-val])
        return -1 if dp[amount]==sys.float_info.max else dp[amount]
