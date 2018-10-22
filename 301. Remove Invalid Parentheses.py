"""No trick here, just brute-force search.

iter 1: if no deletion, see if valid;
iter 2: delete 1 char, see if any subsequence valid;
iter 3: then keep deleting 1 char of the subsequneces, and see if valid
...
Return at any time when any valid subsequence(s) is(are) valid
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            cnt = 0
            for si in s:
                if si == '(':
                    cnt += 1
                elif si == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
        
        candidates = {s}
        while True:
            validStrs = list()
            for candStr in candidates:
                if isValid(candStr):
                    validStrs.append(candStr)
            if len(validStrs) > 0:
                return validStrs
            else:
                candidates = {candStr[:i]+candStr[i+1:] \
                    for candStr in candidates for i in xrange(len(candStr))}
        
