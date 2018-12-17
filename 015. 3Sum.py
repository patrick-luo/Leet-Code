"""They key idea is to sort nums first (the time
complexity will be > nlogn anyway), move the first
index from the begining and then do 2sum for the rest
(using two pointers).

Note: in order to de-duplicate, skip the duplicates
when each pointer is moved. See the comments below.
"""

# a more recent version
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = list()
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                ssum = nums[i]+nums[j]+nums[k]
                if ssum < 0:
                    j += 1
                elif ssum > 0:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    for x in xrange(j+1, k): # x is the next valid j
                        if nums[x] != nums[j]:
                            j = x
                            break
                    else: # if no such valid j
                        break # break the "while j<k" loop
                    for x in xrange(k-1, j, -1):
                        if nums[x] != nums[k]:
                            k = x
                            break
                    else:
                        break
        return ans

# a previous version
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        nums.sort()
        for i in xrange(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]: # skip duplicates!
                lo, hi = i+1, len(nums)-1
                while lo < hi:
                    s = nums[i] + nums[lo] + nums[hi]
                    if s < 0:
                        lo += 1
                    elif s > 0:
                        hi -= 1
                    else:
                        res.append([nums[i], nums[lo], nums[hi]])
                        lo += 1
                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1 # skip duplicates!
                        hi -= 1
                        while lo < hi and nums[hi] == nums[hi+1]:
                            hi -= 1 # skip duplicates!
        return res
