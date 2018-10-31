"""This is a sample solution. 

The key idea is to count how many 'heads' are there."""

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == 'X' and (i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.'):
                    cnt += 1
        return cnt
