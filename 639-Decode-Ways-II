"""The idea is the same as Decode Ways I

The only challenge is to handle wild character '*'.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = int(10e9+7)
        prev2 = 1
        if s[0] == '*':
            prev1 = 9
        else:
            prev1 = 0 if s[0]=='0' else 1
        for i, si in enumerate(s[1:],1):
            if si == '0':
                curr = 0
            elif si == '*':
                curr = prev1 * 9 % mod
            else:
                curr = prev1 % mod
                
            if s[i-1] == '1':
                curr += prev2*9%mod if si=='*' else prev2%mod
            elif s[i-1] == '2':
                if '0'<=si<='6':
                    curr += prev2 % mod
                elif si == '*':
                    curr += prev2*6%mod
            elif s[i-1] == '*':
                if si == '*':
                    curr += prev2*15%mod
                elif '0'<=si<='6':
                    curr += prev2*2%mod
                else:
                    curr += prev2 % mod
            prev2 = prev1
            prev1 = curr
        return int(prev1)
