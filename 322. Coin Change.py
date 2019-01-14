"""This solution didn't pass, but gives the greedy idea"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        if amount < 0:
            return -1
        coins.sort(reverse=True)
        
        def coinRec(coins, amount):
            if len(coins) == 1:
                return -1 if amount%coins[0]!=0 else amount/coins[0]
            cur = coins[0]
            for i in xrange(amount/cur, 0, -1):
                nums = coinRec(coins[1:], amount-i*cur)
                if nums > -1:
                    return i + nums
            return coinRec(coins[1:], amount)
        
        return coinRec(coins, amount)
        
        
        
        
