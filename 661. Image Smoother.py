class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        if m == 0:
            return list()
        n = len(M[0])
        ans = [[0] * n for _ in xrange(m)]
        
        for i in xrange(m):
            for j in xrange(n):
                count = 0
                for a in xrange(i-1, i+2):
                    for b in xrange(j-1, j+2):
                        if 0<=a<m and 0<=b<n:
                            ans[i][j] += M[a][b]
                            count += 1
                ans[i][j] /= count
        return ans
