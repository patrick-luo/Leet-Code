class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        i = 0
        chars = [0] * 128
        cnt = 0
        for j, sj in enumerate(s):
            chars[ord(sj)] += 1
            if chars[ord(sj)] == 1:
                cnt += 1
            while cnt > k:
                chars[ord(s[i])] -= 1
                if chars[ord(s[i])] == 0:
                    cnt -= 1
                i += 1
            ans = max(ans, j-i+1)
        return ans
