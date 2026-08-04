class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        for right in range(len(nums)):
            if nums[right] != nums[left]:
                left +=1
                nums[right] , nums[left] = nums[left] , nums[right]
        return left + 1 

