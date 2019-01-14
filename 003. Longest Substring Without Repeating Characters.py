class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        chars = [False] * 128
        i = 0
        maxLen = 0
        for j, sj in enumerate(s):
            if not chars[ord(sj)]:
                maxLen = max(maxLen, j-i+1)
            else:
                while chars[ord(sj)]:
                    chars[ord(s[i])] = False
                    i += 1
            chars[ord(sj)] = True                
        return maxLen
        
