class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the array has 2 or fewer elements, it already meets the condition
        if len(nums) <= 2:
            return len(nums)
        
        # 'insert_pos' tracks where the next valid element should be placed
        insert_pos = 2
        
        # Start scanning from the 3rd element (index 2)
        for i in range(2, len(nums)):
            # Compare current element with the element 2 positions behind the insert pointer.
            # Since the array is sorted, if they are different, it means the current element
            # hasn't been allowed twice yet.
            if nums[i] != nums[insert_pos - 2]:
                nums[insert_pos] = nums[i]
                insert_pos += 1
                
        return insert_pos