"""
00A 01B
10C 11D

00C 01A
10D 11B

00 to 01   +1
01 to 11   +10
10 to 00   -10
11 to 10   -1


"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        n = len(matrix)
        storage = 0
        for x in range(n):
            for y in range(x+1,n):
                storage = matrix[x][y]
                matrix[x][y] = matrix[y][x]
                matrix[y][x] = storage
