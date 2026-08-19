#34. Find First and Last Position of Element in Sorted Array
#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.If target is not found in the array, return [-1, -1].You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def Lowerbound():
            n=len(nums)-1
            low=0
            high=n-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        def Upperbound():
            n=len(nums)
            low=0
            high=n-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        return[Lowerbound(),Upperbound()]






        