class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # Suppose now all the chars T[:j] have been matched
        # and we are trying to match T[j]. 'cur' list can be
        # understood as a dict() where the key is i such that
        # S[i] == T[j-1] (i.e. the end index of the sub-string in S
        # that matches T[:j]), and the value is the smallest starting
        # index of the sub-string.
        cur = [i if si == T[0] else None for i, si in enumerate(S)]
        
        # At time j when considering T[:j+1],
        # the smallest window [start, end] where S[end] == T[j-1]
        # is represented by cur[end] = start.
        for j in xrange(1, len(T)):
            lastStart = None
            new = [None] * len(S)
            
            # Now we would like to calculate the candidate windows
            # 'new' for T[:j+1].  'lastStart' is the last window start seen.
            for i, si in enumerate(S):
                if lastStart is not None and si == T[j]:
                    new[i] = lastStart
                    
                # Here we keep increasing 'lastStart'
                # to ensure the smallest window start
                if cur[i] is not None:
                    lastStart = cur[i]
            cur = new

        # Looking at the window data 'cur', choose the smallest length
        # window [s, e].
        ans = -1, len(S)
        for end, start in enumerate(cur):
            if start is not None and end-start < ans[1]-ans[0]:
                ans = start, end
        return S[ans[0]: ans[1]+1] if ans[0] != -1 else ''
        
