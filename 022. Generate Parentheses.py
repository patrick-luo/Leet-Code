class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return list()
        if n == 1:
            return ['()']
        
        ans = set()
        for combo in self.generateParenthesis(n-1):
            for i in xrange(len(combo)):
                ans.add(combo[:i]+'()'+combo[i:])
        return list(ans)
            
