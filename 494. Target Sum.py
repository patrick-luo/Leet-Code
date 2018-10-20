class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def put(newSum, memo, ways):
            if newSum not in memo:
                memo[newSum] = ways
            else:
                memo[newSum] += ways
        
        if nums is None or len(nums) == 0:
            return True if S == 0 else False
        memo = {0:1}
        for ni in nums:
            newMemo = dict()
            for mi in memo:
                ways = memo[mi]
                newSum = mi + ni
                put(newSum, newMemo, ways)
                newSum = mi - ni
                put(newSum, newMemo, ways)
            memo = newMemo
        return memo[S] if S in memo else 0
