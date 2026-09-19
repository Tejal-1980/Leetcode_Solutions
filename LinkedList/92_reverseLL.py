# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        Node=[]
        curr=head
        while curr:
            Node.append(curr)
            curr=curr.next
        left-=1
        right-=1
        while left < right:
            Node[left].val, Node[right].val=Node[right].val,Node[left].val
            left+=1
            right-=1
        return head