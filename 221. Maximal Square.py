class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        prevRow = [0] * m
        maxSize = 0
        for row in matrix:
            thisRow = [0] * m
            for j, char in enumerate(row):
                if char == '1':
                    thisRow[j] = 1 if j == 0 else \
                        min([thisRow[j-1], prevRow[j-1], prevRow[j]])+1
                    maxSize = max(maxSize, thisRow[j])
            prevRow = thisRow
        return maxSize ** 2
