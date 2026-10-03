class Solution(object):
    def insertGreatestCommonDivisors(self, head,ListNode):

        curr = head

        while curr and curr.next:

            # Find GCD
            a = curr.val
            b = curr.next.val

            while b:
                a, b = b, a % b

            gcd_value = a

            # Create new node
            new_node = ListNode(gcd_value)

            # Insert new node
            new_node.next = curr.next
            curr.next = new_node

            # Move to original next node
            curr = new_node.next

        return head