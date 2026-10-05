class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for i in nums1:
            index = nums2.index(i)

            for j in nums2[index + 1:]:
                if j > i:
                    ans.append(j)
                    break
            else:
                ans.append(-1)

        return ans