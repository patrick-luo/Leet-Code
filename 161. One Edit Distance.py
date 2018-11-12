class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            replaced = False
            for si, ti in zip(s, t):
                if si != ti:
                    if replaced:
                        return False
                    else:
                        replaced = True
            return replaced
        elif abs(len(s)-len(t)) == 1:
            longer = s if len(s) > len(t) else t
            shorter = t if s == longer else s
            i = 0
            for j in xrange(len(shorter)):
                if longer[i] != shorter[j]:
                    return longer[i+1:] == shorter[j:]
                else:
                    i += 1
            return True
        else:
            return False
            
