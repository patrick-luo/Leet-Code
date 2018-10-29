class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def expand(grid, visited, i, j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and \
                    grid[i][j]=='1' and not visited[i][j]:
                visited[i][j] = True
                expand(grid, visited, i, j+1)
                expand(grid, visited, i, j-1)
                expand(grid, visited, i+1, j)
                expand(grid, visited, i-1, j)
                return 1
            else:
                return 0
        
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        visited = [[False]*len(grid[0]) for i in xrange(len(grid))]
        count = 0
        
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                count += expand(grid, visited, i, j)
        return count
