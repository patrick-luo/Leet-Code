"""A sample solution.

We can split S to two parts for two coordinates.
Then we use sub function f to find all possible strings for each coordinate.

In sub functon f(S)
if S == "": return []
if S == "0": return [S]
if S == "0XXX0": return []
if S == "0XXX": return ["0.XXX"]
if S == "XXX0": return [S]
return [S, "X.XXX", "XX.XX", "XXX.X"...]

Then we add the product of two lists to result.

Time complexity
O(N^3) with N <= 10
"""

class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def sub(s):
            if len(s) == 0 or len(s) > 1 and s[0] == s[-1] == '0':
                return list()
            elif s[-1] == '0':
                return [s]
            elif s[0] == '0':
                return ['0.' + s[1:]]
            else:
                return [s] + [s[:i] + '.' + s[i:] for i in range(1,len(s))]
        
        s = S[1:-1]
        res = list()
        for i in range(1,len(s)):
            left = sub(s[:i])
            if len(left) > 0:
                right = sub(s[i:])
                if len(right) > 0:
                    for l in left:
                        for r in right:
                            res.append('('+l+', '+r+')')
        return res
