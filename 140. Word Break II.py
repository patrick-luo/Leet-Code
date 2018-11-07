"""Not sure why memory limit exceeded, but this solution works"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def postProcess(combos, s):
            if combos is None:
                return list()
            else:
                ans = list()
                for c in combos:
                    words = list()
                    start = 0
                    for end in c:
                        words.append(s[start:end])
                        start = end
                    ans.append(' '.join(words))
                return ans
        
        dp = [None] * (len(s)+1)
        dp[0] = [[]]
        for i in xrange(1, len(dp)):
            combosFori = list()
            for j in xrange(i):
                if dp[j] is not None and s[j:i] in wordDict:
                    for combo in dp[j]:
                        combosFori.append(combo + [i])
            if len(combosFori) > 0:
                dp[i] = combosFori
        return postProcess(dp[len(s)], s)
        
        
