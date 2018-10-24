class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isAlphaNum(c):
            if ord('0') <= ord(c) <= ord('9'):
                return True
            elif ord('a') <= ord(c) <= ord('z'):
                return True
            elif ord('A') <= ord(c) <= ord('Z'):
                return True
            else:
                return False
        
        i, j = 0, len(s)-1
        while i < j:
            if not isAlphaNum(s[i]):
                i += 1
                continue
            if not isAlphaNum(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
