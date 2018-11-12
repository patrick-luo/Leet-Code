class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = dict()
        for i, si in enumerate(s):
            if si not in memo:
                memo[si] = i
            else:
                memo[si] = sys.float_info.max
                
        ans = sys.float_info.max
        for c in memo:
            ans = min(ans, memo[c])
        return -1 if ans==sys.float_info.max else ans
