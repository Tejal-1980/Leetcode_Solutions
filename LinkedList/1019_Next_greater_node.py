# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        result=[]
        stack=[]
        curr=head
        while curr:
            result.append(0)
            while stack and curr.val>result[stack[-1]]:
                index=stack.pop()
                result[index]=curr.val
            stack.append(len(result)-1)
            curr=curr.next
        return result