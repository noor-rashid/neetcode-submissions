class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def matrix_size(matrix):
            cols = len(matrix[0])
            rows = len(matrix)
            return cols*rows

        def position(index, columns):
            return divmod(index,columns)

        low = 0
        high = matrix_size(matrix)-1
        columns = len(matrix[0])

        while low <= high:
            mid = (low+high)//2
            row, col = position(mid, columns)
            guess = matrix[row][col]
            if guess == target:
                return True
            elif guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return False 