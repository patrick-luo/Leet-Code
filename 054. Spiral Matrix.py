class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return list()
        return self.spiral(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1)
        
    def spiral(self, matrix, a, b, x, y):
        m = x-a+1
        if m == 0:
            return list()
        n = y-b+1
        if n == 0:
            return list()
        if m == 1 or n == 1:
            return [e for row in matrix[a:x+1] for e in row[b:y+1]]
        
        ans = list()
        for j in xrange(b, y+1):
            ans.append(matrix[a][j])
        for i in xrange(a+1, x+1):
            ans.append(matrix[i][j])
        for j in xrange(y-1, b-1, -1):
            ans.append(matrix[i][j])
        for i in xrange(x-1, a, -1):
            ans.append(matrix[i][j])
        return ans + self.spiral(matrix, a+1, b+1, x-1, y-1)
