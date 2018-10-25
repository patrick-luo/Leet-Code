class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        memo = dict()
        res = list()
        for ni in nums1:
            if ni in memo:
                memo[ni] += 1
            else:
                memo[ni] = 1
        for ni in nums2:
            if ni in memo and memo[ni] > 0:
                res.append(ni)
                memo[ni] -= 1
        return res
        
