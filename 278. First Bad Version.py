# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while True:
            if isBadVersion(low):
                return low
            mid = low + (high-low)/2
            isBad = isBadVersion(mid)
            if isBad:
                high = mid
            else:
                low = mid + 1
