class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1 if len(nums1)<len(nums2) else nums2
        B = nums2 if A==nums1 else nums1
        m = min(len(A), len(B))
        n = max(len(A), len(B))
        if m == 0 and n == 0:
            return None
        if n == 0:
            return (A[m/2]+A[m/2+1])/2.0 if m%2==0 else A[m/2]
        
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: 
                    max_of_left = B[j-1]
                elif j == 0: 
                    max_of_left = A[i-1]
                else: 
                    max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: 
                    min_of_right = B[j]
                elif j == n: 
                    min_of_right = A[i]
                else: 
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
        
            
