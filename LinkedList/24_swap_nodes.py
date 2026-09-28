class Solution:
  def swapPairs(self,head):
    if head is None and head.next is None:
      return head
    prev=head
    curr=head.next
    
    while curr:
      prev.val , curr.val=curr.val, prev.val
      if curr.next is None:
        break
      prev=curr.next
      curr=prev.next
    return head
    

      
   

