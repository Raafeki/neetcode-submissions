class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            middle_row = (top + bot) // 2
            if target > matrix[middle_row][-1]: # is the target value greater than the largest value in this row?
                top = middle_row + 1
            elif target < matrix[middle_row][0]:
                bot = middle_row - 1
            else:
                break

        
        if not (top <= bot):
            return False

        middle_row = middle_row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l+r) // 2
            if target > matrix[middle_row][m]:
                l = m + 1
            elif target < matrix[middle_row][m]:
                r = m - 1
            else:
                return True
        return False
                