class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, i, j):
            if j==len(s) or s[i] != s[j]:
                return i, i
            while i>0 and j<len(s)-1 and s[i-1]==s[j+1]:
                i -= 1
                j += 1
            return i, j
        
        if len(s) == 0:
            return ''
        start, end = 0, 0
        for i in xrange(len(s)):
            l1, r1 = expand(s, i, i)
            l2, r2 = expand(s, i, i+1)
            if r1-l1 > end-start:
                start, end = l1, r1
            if r2-l2 > end-start:
                start, end = l2, r2
        return s[start:end+1]
