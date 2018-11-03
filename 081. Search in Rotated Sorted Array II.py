class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def bsearch(nums, target, low, high):
            if high < low:
                return False
            mid = (low+high) / 2
            if nums[mid] == target:
                return True
            if nums[low] < nums[mid]: # the left half is ordered
                if nums[low] <= target < nums[mid]:
                    return bsearch(nums, target, low, mid-1)
                else:
                    return bsearch(nums, target, mid+1, high)
            elif nums[low] > nums[mid]: # the right half is ordered
                if nums[mid] < target <= nums[high]:
                    return bsearch(nums, target, mid+1, high)
                else:
                    return bsearch(nums, target, low, mid-1)
            else: # nums[low] == nums[mid]
                # Catch!!! Low and mid are identical, example: {2, 2, 2, 3, 4, 2}.
                # So first check if rightmost element is different: if yes, just search right half;
                if nums[mid] != nums[high]:
                    return bsearch(nums, target, mid+1, high)
                else:
                    # Otherwise, it is the worst case, check both halves.
                    leftFound = bsearch(nums, target, low, mid-1)
                    if leftFound:
                        return True
                    else:
                        return bsearch(nums, target, mid+1, high)
        
        
        return bsearch(nums, target, 0, len(nums)-1)
                
