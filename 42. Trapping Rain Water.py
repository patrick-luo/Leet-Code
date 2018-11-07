class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        
        # A stack of heights. Whenever there's a lower
        # height than peek, push it in. So the heights
        # stored in this stack are non-increasing.
        stackH = list()
        
        # A stack of the most recent locations
        # of the heights
        stackLoc = list()
        
        for i, hi, in enumerate(height):
            if len(stackH) == 0 or hi < stackH[-1]:
                stackH.append(hi)
                stackLoc.append(i)
            elif hi == stackH[-1]:
                stackLoc[-1] = i
            else:
                bottom = stackH.pop()
                loc = stackLoc.pop()
                while bottom < hi and len(stackH) > 0:
                    hDiff = min(stackH[-1], hi) - bottom
                    locDiff = i - stackLoc[-1] - 1
                    bottom = stackH.pop()
                    loc = stackLoc.pop()
                    ans += hDiff * locDiff
                if bottom > hi:
                    stackH.append(bottom)
                    stackLoc.append(loc)
                stackH.append(hi)
                stackLoc.append(i)
        
        return ans
