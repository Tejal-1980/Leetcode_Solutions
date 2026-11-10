class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack=[]
        for num in nums:
            if stack and stack[-1]==num:
                stack.pop()
            else:
                stack.append(num)
        return stack[0]
        