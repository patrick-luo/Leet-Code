class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        def found(board, i, j, word, used):
            if len(word) == 0:
                return True
            if 0<=i<len(board) and 0<=j<len(board[0]) \
                    and not used[i][j] and board[i][j] == word[0]:
                used[i][j] = True
                for a, b in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if found(board, a, b, word[1:], used):
                        return True
                used[i][j] = False
            return False
                    
        
        used = [[False]*len(board[0]) for _ in xrange(len(board))]
        for i, row in enumerate(board):
            for j, e in enumerate(row):
                if found(board, i, j, word, used):
                    return True
        return False
                    
