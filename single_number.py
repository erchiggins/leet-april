class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index, num in enumerate(nums):
            if num not in nums[index+1:] and num not in nums[:index]:
                return num
