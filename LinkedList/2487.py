class Solution:
    def removeNodes(self, head):
        # Reverse the linked list
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Remove smaller nodes
        curr = prev
        max_value = 0
        new_head = None

        while curr:
            if curr.val >= max_value:
                max_value = curr.val

                next_node = curr.next
                curr.next = new_head
                new_head = curr
                curr = next_node
            else:
                curr = curr.next

        return new_head