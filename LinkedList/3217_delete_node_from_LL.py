# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head , ListNode):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums=set(nums)
        dummy = ListNode(0)
        dummy.next=head
        curr=head
        prev=dummy
        while curr is not None:
            if curr.val in nums:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.nexts