# Find missing number

# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.
class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum