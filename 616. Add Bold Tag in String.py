class Solution(object):
    def addBoldTag(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        bold = [False] * len(s)
        end = 0
        for i in xrange(len(s)):
            for word in d:
                if s[i:].startswith(word):
                    end = max(end, i+len(word))
            if i < end:
                bold[i] = True
        
        ans = list()
        i = 0
        for i in xrange(len(s)):
            if bold[i]:
                if i==0 or not bold[i-1]:
                    ans.append('<b>')
                ans.append(s[i])
                if i==len(s)-1 or not bold[i+1]:
                    ans.append('</b>')
            else:
                ans.append(s[i])
        return ''.join(ans)
