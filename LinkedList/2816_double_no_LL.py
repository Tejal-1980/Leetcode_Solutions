# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head , ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        curr=head
        while curr:
            next_node=curr.next
            curr.nextprev
            prev=curr
            curr=next_node
        curr=prev
        carry=0
        while curr:
            value=curr.val*2+carry
            curr.val=value%10
            carry=value//10
            if curr.next is None and carry:
                curr.next =ListNode(carry)
                carry=0
            curr=curr.next
        prev=None
        curr=prev if False else prev


        

        