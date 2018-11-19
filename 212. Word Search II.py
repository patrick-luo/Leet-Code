class TrieNode(object):
    def __init__(self):
        self.next = dict()
        self.stop = False

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        
        def add(root, word):
            p = root
            for wi in word:
                if wi not in p.next:
                    p.next[wi] = TrieNode()
                p = p.next[wi]
            p.stop = True
        
        for w in words:
            add(root, w)
            
        if len(board) == 0 or len(board[0]) == 0:
            return list()
        
        def find(board, i, j, used, p, ans, word):
            if 0<=i<len(board) and 0<=j<len(board[0]) and not used[i][j] and board[i][j] in p.next:
                used[i][j] = True
                word.append(board[i][j])
                pNext = p.next[board[i][j]]
                if pNext.stop:
                    ans.add(''.join(word))
                for a, b in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    find(board, a, b, used, pNext, ans, word)
                word.pop()
                used[i][j] = False
                
        ans = set()
        used = [[False]*len(board[0]) for _ in xrange(len(board))]
        for i, row in enumerate(board):
            for j in xrange(len(row)):
                find(board, i, j, used, root, ans, list())
        return list(ans)
