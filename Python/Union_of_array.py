#Union of two sorted arrays
# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.
# The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.
class Solution:
    def unionArray(self, nums1, nums2):
        arr = list(set(nums1) | set(nums2))
        arr.sort()
        return arr  



    # Two-pointer method technique
    # class Solution:
    # def unionArray(self, nums1, nums2):
    #     i = 0
    #     j = 0
    #     ans = []

    #     while i < len(nums1) and j < len(nums2):
    #         if nums1[i] < nums2[j]:
    #             if not ans or ans[-1] != nums1[i]:
    #                 ans.append(nums1[i])
    #             i += 1

    #         elif nums1[i] > nums2[j]:
    #             if not ans or ans[-1] != nums2[j]:
    #                 ans.append(nums2[j])
    #             j += 1

    #         else:
    #             if not ans or ans[-1] != nums1[i]:
    #                 ans.append(nums1[i])
    #             i += 1
    #             j += 1

    #     while i < len(nums1):
    #         if not ans or ans[-1] != nums1[i]:
    #             ans.append(nums1[i])
    #         i += 1

    #     while j < len(nums2):
    #         if not ans or ans[-1] != nums2[j]:
    #             ans.append(nums2[j])
    #         j += 1

    #     return ans