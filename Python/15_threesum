class Solution(object):
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1

                elif total > 0:
                    k -= 1
