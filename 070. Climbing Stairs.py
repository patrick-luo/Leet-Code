class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pprev, prev = 0, 1
        for i in xrange(n):
            cur = pprev + prev
            pprev, prev = prev, cur
        return prev
