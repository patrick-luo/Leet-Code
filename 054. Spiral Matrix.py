class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n == 0:
            return list()
        m = len(matrix[0])
        if m == 0:
            return list()
        
        def spiral(mat, i, j, x, y):
            if i > x or j > y:
                return list()
            if i == x or j == y:
                return [e for row in mat[i:x+1] for e in row[j:y+1]]
            ans = list()
            for k in xrange(j, y+1):
                ans.append(mat[i][k])
            for k in xrange(i+1, x+1):
                ans.append(mat[k][y])
            for k in xrange(y-1, j-1, -1):
                ans.append(mat[x][k])
            for k in xrange(x-1, i, -1):
                ans.append(mat[k][j])
            ans.extend(spiral(mat, i+1, j+1, x-1, y-1))
            return ans
            
        return spiral(matrix, 0, 0, n-1, m-1)
  
