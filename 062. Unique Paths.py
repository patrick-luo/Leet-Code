class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        prevRow = [0] * m
        for i in xrange(n):
            row = [1]
            for j in xrange(1, m):
                row.append(row[-1] + prevRow[j])
            prevRow = row
        return prevRow[-1]
