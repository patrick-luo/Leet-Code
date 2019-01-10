class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def comparator(s, t):
            return 1 if s+t<t+s else -1
        
        strs = [str(n) for n in nums]
        strs.sort(cmp=comparator)
        ans = ''.join(strs)
        return '0' if ans[0]=='0' else ans
        
