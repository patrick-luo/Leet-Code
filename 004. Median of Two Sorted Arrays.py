"""
The general idea is to find i in the shorted list (A) and
j in the longer list (B), and divide the lists into:
A[0],...,A[i-1] <= A[i],...,A[m-1]
B[0],...,B[j-1] <= B[j],...,B[n-1]
such that A[i-1] <= B[j] and B[j-1] <= A[i]
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # step 1: find the shorter and longer list
        A = nums1 if len(nums1)<len(nums2) else nums2
        B = nums2 if A==nums1 else nums1
        m = min(len(A), len(B))
        n = max(len(A), len(B))
        if n == 0:
            return None
        
        # step 2: find the right location of i
        imin, imax, halfLen = 0, m, (m+n+1)/2 # add one more 1
        while imin <= imax:
            i = (imin+imax) / 2
            j = halfLen - i
            if i > 0 and A[i-1] > B[j]:
                # i is too large
                # check i > 0 because next we will decrease imax
                imax = i - 1
            elif i < m and B[j-1] > A[i]:
                # i is too small
                # check i < m because next we will increase imin
                imin = i + 1
            else:
                # i is perfect
                
                # in order to have 'leftmax = max(A[i-1], B[j-1])', check if i-1 or j-i is valid
                if i == 0:
                    leftmax = B[j-1]
                elif j == 0:
                    leftmax = A[i-1]
                else:
                    leftmax = max(A[i-1], B[j-1])
                
                if (m+n)%2==1:
                    return leftmax
                
                # in order to have 'rightmin = min(A[i], B[j])', check if i or j is valid
                if i == m:
                    rightmin = B[j]
                elif j == n:
                    rightmin = A[i]
                else:
                    rightmin = min(A[i], B[j])
                    
                return (leftmax+rightmin) / 2.0
                
                
