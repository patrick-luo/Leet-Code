
"""This recursive solution is time limit exceeded,
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
        
        if s[0] not in {'?','*'} and p[0] not in {'?','*'}:
            return s[0] == p[0] and self.isMatch(s[1:], p[1:])
        if s[0]!='*' and p[0]!='*' and s[0]=='?' or p[0]=='?':
            return self.isMatch(s[1:], p[1:])
        if s[0]=='*' and p[0]=='*':
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p) \
                or self.isMatch[s[1:], p[1:]]
        if s[0]=='*' or p[0]=='*':
            star = s if s[0]=='*' else p
            norm = s if p==star else p
            return self.isMatch(norm, star[1:]) or self.isMatch(norm[1:], star[1:]) \
                or self.isMatch(norm[1:], star)
        
        
