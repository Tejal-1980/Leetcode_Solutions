class Solution(object):
    def swapNodes(self, head, k):

        # Find kth node from beginning
        first = head

        for i in range(k - 1):
            first = first.next

        # Find kth node from end
        second = head
        fast = first

        while fast.next:
            fast = fast.next
            second = second.next

        # Swap values
        first.val, second.val = second.val, first.val

        return head