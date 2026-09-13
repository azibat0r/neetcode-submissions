class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        answer = False

        def backtracking(row, col, idx):
            if idx == len(word):
                return True

            if row < 0 or row == len(board) or col < 0 or col == len(board[0]):
                return False

            char = word[idx]
            pos = board[row][col]

            if pos != char:
                return False

            board[row][col] = "used"

            idx += 1
            check1 = backtracking(row+1, col, idx)
            check2 = backtracking(row-1, col, idx)
            check3 = backtracking(row, col+1, idx)
            check4 = backtracking(row, col-1, idx)

            board[row][col] = char

            if check1 or check2 or check3 or check4:
                return True
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtracking(row, col, 0):
                    answer = True

        return answer