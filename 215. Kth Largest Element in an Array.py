class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def semiQsort(nums, low, high, k):
            i, j = low, high
            pivot = nums[(low+high)/2]
            while True:
                while nums[i] > pivot:
                    i += 1
                while nums[j] < pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                if i > j:
                    break
            # l<=r ensures it's OK to sort
            # i<=k<=r means it's necessary to sort
            if low <= k <= j:
                semiQsort(nums, low, j, k)
            if i <= k <= high:
                semiQsort(nums, i, high, k)
                
        semiQsort(nums, 0, len(nums)-1, k-1)
        return nums[k-1]


