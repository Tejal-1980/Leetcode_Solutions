# 2149. Rearrange Array Elements by Sign
# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.You should return the array of nums such that the array follows the given conditions: Every consecutive pair of integers have opposite signs.For all integers with the same sign, the order in which they were present in nums is preserved.The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=[]
        right=[]
        for i in nums:
            if i > 0:
                left.append(i)
            else:
                right.append(i)
        ans=[]
        for i in range(len(left)):
            ans.append(left[i])
            ans.append(right[i])
        return ans
            