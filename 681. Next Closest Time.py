"""This is a refactored cleaner version"""

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def output(nums):
            for i, n in enumerate(nums):
                nums[i] = str(n)
            return nums[0]+nums[1]+':'+nums[2]+nums[3]
        
        def ansFound(i, ub, nums):
            for n in xrange(nums[i]+1, ub):
                if n in nums:
                    for j in xrange(i+1, 4):
                        nums[j] = min(nums)
                    nums[i] = n
                    return True
            return False
                        
        
        pair = time.split(':')
        nums = [int(pair[0][0]), int(pair[0][1]), int(pair[1][0]), int(pair[1][1])]
        
        if ansFound(3, 10, nums):
            return output(nums)
        if ansFound(2, 6, nums):
            return output(nums)
        ub2ndMin = 10 if nums[0] in {0, 1} else 4
        if ansFound(1, ub2ndMin, nums):
            return output(nums)
        if ansFound(0, 3, nums):
            return output(nums)
        return output([min(nums)]*4)
            
            


"""This is my original coding"""
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def output(nums):
            for i, n in enumerate(nums):
                nums[i] = str(n)
            return nums[0]+nums[1]+':'+nums[2]+nums[3]
        
        pair = time.split(':')
        nums = [int(pair[0][0]), int(pair[0][1]), int(pair[1][0]), int(pair[1][1])]
        
        for n in xrange(nums[3]+1, 10):
            if n in nums:
                nums[3] = n
                return output(nums)
        for n in xrange(nums[2]+1, 6):
            if n in nums:
                nums[3] = min(nums)
                nums[2] = n
                return output(nums)
        if nums[0] in {0, 1}:
            for n in xrange(nums[1]+1, 10):
                if n in nums:
                    nums[2] = min(nums)
                    nums[3] = min(nums)
                    nums[1] = n
                    return output(nums)
            for n in xrange(nums[0]+1, 3):
                if n in nums:
                    nums[1] = min(nums)
                    nums[2] = min(nums)
                    nums[3] = min(nums)
                    nums[0] = n
                    return output(nums)
            return output([min(nums)]*4)
        else:
            for n in xrange(nums[1]+1, 5):
                if n in nums:
                    nums[2] = min(nums)
                    nums[3] = min(nums)
                    nums[1] = n
                    return output(nums)
            for n in xrange(nums[0]+1, 3):
                if n in nums:
                    nums[1] = min(nums)
                    nums[2] = min(nums)
                    nums[3] = min(nums)
                    nums[0] = n
                    return output(nums)
            return output([min(nums)]*4)
            
            
