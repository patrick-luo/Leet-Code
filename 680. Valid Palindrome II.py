class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def valid(s, left, right, delete):
            while left < right:
                if s[left] != s[right]:
                    if delete:
                        return valid(s, left+1, right, False) \
                            or valid(s, left, right-1, False)
                    else:
                        return False
                left += 1
                right -= 1
            return True
        
        return valid(s, 0, len(s)-1, True)
