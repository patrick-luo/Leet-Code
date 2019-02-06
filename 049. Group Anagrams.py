class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = dict()
        for s in strs:
            count = [0] * 26
            for si in s:
                count[ord(si)-ord('a')] += 1
            key = tuple(count)
            if key not in ans:
                ans[key] = list()
            ans[key].append(s)
        return ans.values()
            
