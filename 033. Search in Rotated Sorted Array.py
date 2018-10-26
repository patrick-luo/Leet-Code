class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low)/2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid] <= nums[-1]: # no rotation
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[mid] >= nums[0] and nums[mid] > nums[-1]: # mid on the left increasing branch
                if nums[mid] < target:
                    low = mid + 1
                else: # worst case linear search
                    if nums[low] == target:
                        return low
                    else:
                        low += 1
            elif nums[mid] < nums[0] and nums[mid] <= nums[-1]: # mid on the right increasing branch
                if nums[mid] > target:
                    high = mid - 1
                else: # worst case linear search
                    if nums[high] == target:
                        return high
                    else:
                        high -= 1
        return -1
