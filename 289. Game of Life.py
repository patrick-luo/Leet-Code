class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def neighbor(board, i, j):
            cnt = 0
            for a in xrange(i-1, i+2):
                for b in xrange(j-1, j+2):
                    if a>=0 and b>=0 and a<len(board) and b<len(board[0]) and not (i==a and j==b) \
                            and (board[a][b]==1 or board[a][b]!=0 and board[a][b][0]=='1'):
                        cnt += 1
            return cnt
        
        for i, row in enumerate(board):
            for j in xrange(len(row)):
                count = neighbor(board, i, j)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = '1->0'
                    else:
                        board[i][j] = '1->1'
                else:
                    if count == 3:
                        board[i][j] = '0->1'
                    else:
                        board[i][j] = '0->0'
        
        for i, row in enumerate(board):
            for j in xrange(len(row)):
                board[i][j] = int(board[i][j][3])
