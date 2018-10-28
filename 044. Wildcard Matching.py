"""This is an accepted DP solution"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def initDPMatrice(m, n):
            f = list()
            for i in xrange(m):
                f.append([False]*n)
            return f
        
        # This matrix entry f[i][j] tells the first
        # i chars of s can be matched to the first
        # j chars of p.
        f = initDPMatrice(len(s)+1, len(p)+1)
        f[0][0] = True;
        
        for i in xrange(len(s)+1):
            for j in xrange(len(p)+1):
                # we always have "f[i][j] = f[i][j] or ..."
                # because the value of f[i][j]
                # can be updated in multiple 'if' conditions
                
                # case 1: use the current '*' for p, and
                # still use it in the sub-comparison in f[i-1][j]
                if j > 0 and i > 0 and p[j-1] == '*':
                    f[i][j] = f[i][j] or f[i-1][j]
                    
                # case 2: don't use the current '*' for p
                if j > 0 and p[j-1] == '*':
                    f[i][j] = f[i][j] or f[i][j-1]
                
                # case 3: consuming one char for both s and p
                if j > 0 and i > 0 and (p[j-1] == '*' or p[j-1] == '?' or s[i-1] == p[j-1]):
                    f[i][j] = f[i][j] or f[i-1][j-1];
        return f[len(s)][len(p)];
        
        



"""This recursive solution is time limit exceeded
(because there are too many duplicate comparisons
in the recursive functions),
but can give the general idea."""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) + len(p) == 0:
            return True
        if len(s) * len(p) == 0:
            notEmpty = p if len(s)==0 else s
            for c in notEmpty:
                if c != '*':
                    return False
            return True
        
        if p[0] == '*':
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p[1:]) or self.isMatch(s[1:], p)
        elif p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        else: # an ordinary char
            return s[0] == p[0] and self.isMatch(s[1:], p[1:])
        
        
