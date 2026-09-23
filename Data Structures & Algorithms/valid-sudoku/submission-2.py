"""
make 3 dictionaries

1. key = row, so item is all digists in row i.e 1
2. smae for columns
3. key = tuple of (x,x)
so the borad has 9 squares
(0,0) reps square at top left
(0,1) reps square at top middle and so on
so they key hold all items in square

row = defaultdict(set)



"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue

                if board[x][y] in row[x]:
                    return False
                else:
                    row[x].add(board[x][y])
        for y in range(9):
            for x in range(9):
                if board[x][y] == ".":
                    continue
                if board[x][y] in col[y]:
                    return False
                else:
                    col[y].add(board[x][y])

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if board[x][y] in square[(x//3,y//3)]:
                    return False
                else:
                    square[(x//3,y//3)].add(board[x][y])

        return True