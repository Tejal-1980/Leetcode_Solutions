class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answers = [1] * n

        for i in range(1, n):
            answers[i] = answers[i - 1] * nums[i - 1]

        right = 1

        for i in range(n - 1, -1, -1):
            answers[i] = answers[i] * right
            right *= nums[i]

        return answers
