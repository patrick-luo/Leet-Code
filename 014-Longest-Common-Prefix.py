"This is a sample solution"

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        shortest = min(strs, key=lambda s:len(s))
        for i, si in enumerate(shortest):
            for other in strs:
                if si != other[i]:
                    return other[:i]
        return shortest
       

        
