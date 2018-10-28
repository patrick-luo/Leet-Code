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
        
        pc = list() # store the non-start chars
        pn = list() # tell if each char in pc can is followed by '*' or not
        for c in p:
            if c != '*':
                pc.append(c)
                pn.append(False)
            else:
                pn[-1] = True
        
        # This matrice f[i][j] tells if
        # the first i chars in s are matched
        # with the first j chars in pc.
        f = initDPMatrice(len(s)+1, len(pc)+1)
        f[0][0] = True
        
        for i in xrange(len(s)+1):
            for j in xrange(len(pc)+1):
                # we always have "f[i][j] = f[i][j] or ..."
                # because f[i][j] can be modified by
                # multiple 'if' conditions
                if i > 0 and j > 0 and (pc[j-1] == s[i-1] or pc[j-1] == '.'):
                    f[i][j] = f[i][j] or f[i-1][j-1]
                if i > 0 and j > 0 and (pc[j-1] == s[i-1] or pc[j-1] == '.') and pn[j-1]:
                    f[i][j] = f[i][j] or f[i-1][j]
                if j > 0 and pn[j-1]:
                    f[i][j] = f[i][j] or f[i][j-1]

        return f[len(s)][len(pc)];
