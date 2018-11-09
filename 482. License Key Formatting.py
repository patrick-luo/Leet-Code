"""Something wrong with Leetcode's testing"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        parts = S.split('-')
        words = list()
        buff = list()
        for i in xrange(len(parts)-1, -1, -1):
            p = parts[i]
            for j in xrange(len(p)-1, -1, -1):
                buff.append(p[j].upper())    
                if len(buff) == K:
                    buff.reverse()
                    words.append(''.join(buff))
                    del buff[:]
        buff.reverse()
        words.append(''.join(buff))
        ans = words[-1]
        for i in xrange(len(words)-2, -1, -1):
            ans += '-' + words[i]
        return ans
