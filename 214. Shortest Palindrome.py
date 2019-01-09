"""A valid O(N^2) solution, but not sure
why time limit exceeded."""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalin(s):
            i = 0
            j = len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True
        
        if len(s) == 0:
            return s
        
        for i in xrange(len(s), 0, -1):
            if isPalin(s[:i]): # check the longest prefix that is palindrome
                more = list() # then add the rightmore characters reversely to the left
                for j in xrange(len(s)-1, i-1, -1):
                    more.append(s[j])
                return ''.join(more) + s
