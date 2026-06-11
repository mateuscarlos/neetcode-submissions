class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        start, end = 0, COLS - 1
        while start <= end:
            middle = start + (end - start) // 2
            if target > matrix[row][middle]:
                start = middle + 1
            elif target < matrix[row][middle]:
                end = middle - 1
            else:
                return True
        return False