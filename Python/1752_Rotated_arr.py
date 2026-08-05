#1752. Check if Array Is Sorted and Rotated
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        count =0
        for i in range(n):
            if nums[i]>nums[(i+1)% n]: # % makes the comparison circular
                count+=1
        return count<=1