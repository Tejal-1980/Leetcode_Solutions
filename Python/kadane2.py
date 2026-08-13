
# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray. A subarray is a contiguous non-empty sequence of elements within an array.
class Solution:
    def maxSubArray(self, nums):
        total = 0
        largest = float("-inf")

        for num in nums:
            total = total + num
            largest = max(largest, total)

            if total < 0:
                total = 0

        return largest