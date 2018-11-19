class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        def found(board, i, j, word, used):
            if len(word) == 0:
                return True
            for a, b in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0<=a<len(board) and 0<=b<len(board[0]) \
                        and not used[a][b] and board[a][b]==word[0]:
                    used[a][b] = True
                    if found(board, a, b, word[1:], used):
                        return True
                    used[a][b] = False
            return False
                    
        
        used = [[False]*len(board[0]) for _ in xrange(len(board))]
        for i, row in enumerate(board):
            for j, e in enumerate(row):
                if e == word[0]:
                    used[i][j] = True
                    if found(board, i, j, word[1:], used):
                        return True
                    used[i][j] = False
        return False
                    
