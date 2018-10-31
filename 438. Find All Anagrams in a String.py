class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counts = [0] * 26
        for pi in p:
            counts[ord(pi)-ord('a')] += 1
        cnt = len(p)
        i = 0
        ans = list()
        for j, sj in enumerate(s):
            counts[ord(sj)-ord('a')] -= 1
            if counts[ord(sj)-ord('a')] >= 0:
                cnt -= 1
            while cnt == 0:
                if j-i+1 == len(p):
                    ans.append(i)
                counts[ord(s[i])-ord('a')] += 1
                if counts[ord(s[i])-ord('a')] > 0:
                    cnt += 1
                i += 1
        return ans
