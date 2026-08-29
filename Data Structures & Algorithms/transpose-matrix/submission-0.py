class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])

        result = []
        for col in range(column):
            new_row = []
            for rw in range(row):
                new_row.append(matrix[rw][col])
            result.append(new_row)
        return result