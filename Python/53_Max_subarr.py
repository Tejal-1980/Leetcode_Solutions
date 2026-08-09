class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        maxi=float("-inf")
        n=len(nums)
        for i in range(0, n):
            sum+=nums[i]
            maxi=max(maxi,sum)
            if sum<0:
                sum = 0
        return maxi