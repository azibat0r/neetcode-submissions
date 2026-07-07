class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()          # ← reset here, fresh set for each row
            for j in range(len(board[i])):
                a = board[i][j]
                if a != '.':
                    if a in s:
                        return False
                    s.add(a)

        for i in range(len(board)):
            s = set()          # ← reset here, fresh set for each row
            for j in range(len(board[i])):
                a = board[j][i]
                if a != '.':
                    if a in s:
                        return False
                    s.add(a)
        boxes = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                a = board[i][j]
                if a != '.':
                    key = (i//3, j//3)
                    if a in boxes[key]:
                        return False
                    boxes[key].add(a)

        return True
