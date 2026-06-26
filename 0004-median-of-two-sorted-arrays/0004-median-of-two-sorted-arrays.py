class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to optimize binary search space to O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        low, high = 0, len(A)
        
        while low <= high:
            i = (low + high) // 2  # Partition index for A
            j = half - i           # Partition index for B
            
            # Boundary values around partitions (handle out-of-bounds with infinity)
            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < len(B) else float('inf')
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # If total length is odd
                if total % 2:
                    return min(Aright, Bright)
                # If total length is even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                high = i - 1  # Too many elements from A's left side, move left
            else:
                low = i + 1   # Too few elements from A's left side, move right
        