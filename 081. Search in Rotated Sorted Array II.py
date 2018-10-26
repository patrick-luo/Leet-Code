"""The current implementation is not working properly,
but can show the idea.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def bsearch(nums, target, low, high):
            while low <= high:
                mid = low + (high-low)/2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        
        def findPivot(nums):
            low, high = 0, len(nums)-1
            while low <= high:
                if nums[low] < nums[high]:
                    return None
                mid = low + (high-low)/2
                if mid == len(nums) - 1:
                    return None
                if nums[mid] > nums[mid+1]:
                    return mid
                if nums[mid] < nums[high]:
                    high = mid - 1
                elif nums[mid] > nums[low]:
                    low = mid + 1
                else:
                    if low == len(nums) - 1:
                        return None
                    if nums[low] > nums[low+1]:
                        return low
                    else:
                        low += 1
        
        
        pivot = findPivot(nums)
        if pivot is None:
            return bsearch(nums, target, 0, len(nums)-1)
        else:
            if nums[0] <= target <= nums[pivot]:
                return bsearch(nums, target, 0, pivot)
            elif nums[pivot+1] <= target <= nums[-1]:
                return bsearch(nums, target, pivot+1, len(nums)-1)
            else:
                return False
