class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Do one pass to calculate the
        # sum of windows with length K
        # i.e. W[i] = sum(nums[i:i+K])
        W = list()
        ssum = 0
        for i, n in enumerate(nums):
            ssum += n
            if i >= K:
                ssum -= nums[i-K]
            if i >= K-1:
                W.append(ssum)

        # Here left[i] means what's the
        # best index with largest sum in W[:i+1]
        left = [0] * len(W)
        best = 0
        for i in xrange(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        # Similar definiation for 'right'
        right = [0] * len(W)
        best = len(W) - 1
        for i in xrange(len(W)-1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        # Finally, the main program: for the middle
        # W[j], find the max sum of W[i]+W[j]+W[k]
        # where 0<=i<=j-K and j+K<=k<=len(W)-1
        ans = None
        for j in xrange(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or W[i]+W[j]+W[k] > W[ans[0]]+W[ans[1]]+W[ans[2]]:
                ans = i, j, k
        return ans
