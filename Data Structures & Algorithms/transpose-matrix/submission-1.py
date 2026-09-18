class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # get the length of the rows/cols of the original matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # create the new transpose matrix based off these lengths
        res = [[0] * ROWS for _ in range(COLS)]


        # for the rows in the range of OG rows
        for r in range(ROWS):

            # for the cols in the range of the OG cols
            for c in range(COLS):

                # do a simple swap
                res[c][r] = matrix [r][c]


        return res