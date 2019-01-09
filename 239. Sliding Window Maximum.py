class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        q = deque() # this q stores indexes and q[0] is always the largest index
        ans = list()
        
        for end, ni in enumerate(nums):
            if len(q)>0 and q[0]==end-k: # normal pop out
                q.popleft()
            while len(q)>0 and nums[q[-1]]<ni: # flush out those numbers smaller than the current end number
                q.pop()
            q.append(end)
            
            if end >= k-1:
                ans.append(nums[q[0]])
                
        return ans
    
    
    
