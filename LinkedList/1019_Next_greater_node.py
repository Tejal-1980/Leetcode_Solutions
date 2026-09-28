class Solution(object):
    def nextLargerNodes(self, head):
        result = []
        stack = []
        curr = head

        while curr:
            result.append(0)

            while stack and curr.val > stack[-1][1]:
                index, value = stack.pop()
                result[index] = curr.val

            stack.append((len(result) - 1, curr.val))
            curr = curr.next

        return result