class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # Store running prefix sums starting with 0 to handle boundary conditions easily
        self.pref = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.pref[i + 1] = self.pref[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Range sum from index left to right (inclusive)
        return self.pref[right + 1] - self.pref[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)