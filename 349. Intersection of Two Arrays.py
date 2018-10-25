class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        memo = dict() # key is the number, value is whether it has been already in the result list 'res'
        res = list()
        for ni in nums1:
            memo[ni] = False
        for ni in nums2:
            if ni in memo and not memo[ni]:
                res.append(ni)
                memo[ni] = True
        return res
        
