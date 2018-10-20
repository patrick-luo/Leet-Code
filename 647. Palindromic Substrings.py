class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        res = 0
        for center in xrange(2*len(s)):
            left = center / 2
            right = left + center%2
            while left >= 0 and right < len(s) and \
                    s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res
