class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        column = len(matrix[0])

        left = 0
        right = rows * column - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // column
            col = mid % column

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
