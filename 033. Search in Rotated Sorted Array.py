class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high) / 2
            if target == nums[mid]:
                return mid
            
            # case 1: no rotation
            if nums[low] <= nums[mid] <= nums[high]:
                if target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            # case 2: mid on the left increasing branch
            elif nums[high] <= nums[low] <= nums[mid]:
                if target > nums[mid]:
                    low = mid + 1
                else:
                    if nums[low] == target:
                        return low
                    else:
                        low += 1
            # case 3: mid on the right increasing branch
            elif nums[mid] <= nums[high] <= nums[low]:
                if target < nums[mid]:
                    high = mid - 1
                else:
                    if nums[high] == target:
                        return high
                    else:
                        high -= 1
        return -1
                        
