class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        ssum = 0
        # the key is the cumulative sum from nums[0] to nums[i] for some i,
        # value is the count of how many such 'i'
        sumToCnts = {0:1}
        for ni in nums:
            ssum += ni
            if (ssum-k) in sumToCnts:
                count += sumToCnts[ssum-k] # here is ssum-k!!!
            if ssum not in sumToCnts:
                sumToCnts[ssum] = 1
            else:
                sumToCnts[ssum] += 1
        return count
