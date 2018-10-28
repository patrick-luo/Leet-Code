class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt = len(t) # count of how many chars in T are to be consumed
        chars = [0] * 128 # means which chars (and their counts) are to be consumed
        for ti in t:
            chars[ord(ti)] += 1
        minWin = sys.maxint
        start = 0 # the current start index
        head = None # the head of the minimum string
        
        for end, si in enumerate(s):
            chars[ord(si)] -= 1
            if chars[ord(si)] >= 0:
                cnt -= 1
            while cnt == 0:
                if end-start+1 < minWin:
                    minWin = end-start+1
                    head = start
                chars[ord(s[start])] += 1
                if chars[ord(s[start])] > 0:
                    cnt += 1
                start += 1
        return '' if head == None else s[head:head+minWin]
