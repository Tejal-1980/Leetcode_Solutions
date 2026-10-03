class Solution(object):
    def doubleIt(self, head,ListNode):

        # 1. Reverse the list
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 2. Double the reversed list
        curr = prev
        carry = 0

        while curr:
            value = curr.val * 2 + carry
            curr.val = value % 10
            carry = value // 10

            if curr.next is None:
                break

            curr = curr.next

        # 3. If carry remains, add a new node
        if carry:
            curr.next = ListNode(carry)

        # 4. Reverse again
        new_head = None
        curr = prev

        while curr:
            next_node = curr.next
            curr.next = new_head
            new_head = curr
            curr = next_node

        return new_head