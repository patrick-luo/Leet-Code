class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def semiQsort(a, l, r, k):
            i = l
            j = r
            m = a[(l+r)/2] # the pivot number
            while True:
                while a[i] > m:
                    i += 1
                while a[j] < m:
                    j -= 1
                if i <= j:
                    a[i], a[j] = a[j], a[i]
                    i += 1
                    j -= 1
                if i > j:
                    break
            # l<r ensures it's OK to sort
            # i<=k<=r means it's necessary to sort
            if i < r and i <= k <= r:
                semiQsort(a, i, r, k) # sort the right half
            if l < j and l <= k <= j:
                semiQsort(a, l, j, k) # sort the left half
        
        semiQsort(nums, 0, len(nums)-1, k-1)
        return nums[k-1]
