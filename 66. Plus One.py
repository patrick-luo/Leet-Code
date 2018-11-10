class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(digits)-1, -1, -1):
            if digits[i] != 9:
                ans = digits[:i]
                ans.append(digits[i]+1)
                ans += [0] * (len(digits)-i-1)
                return ans
        else:
            return [1] + [0] * len(digits)
