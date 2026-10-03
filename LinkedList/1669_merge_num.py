class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):

        # Find the node at index a-1
        prev = list1
        for i in range(a - 1):
            prev = prev.next

        # Find the node at index b+1
        after = prev.next
        for i in range(b - a + 1):
            after = after.next

        # Connect node before a to list2
        prev.next = list2

        # Find the last node of list2
        tail = list2
        while tail.next:
            tail = tail.next

        # Connect list2 to node after b
        tail.next = after

        return list1