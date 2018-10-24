class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        pprev = 1 # the # of decoding ways for the previous previous digit
        prev = 0 if s[0]=='0' else 1 # the # of decoding ways for the previous digit
        for i, si in enumerate(s[1:],1):
            cur = 0 if si=='0' else prev
            if s[i-1]=='1' or s[i-1]=='2' and '0'<=si<='6':
                cur += pprev
            prev, pprev = cur, prev
        return prev
