class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        Up = 0
        Bottom = len(matrix)
        Right = len(matrix[0])
        Left = 0
        result = []
        y = 0
        x = 0
        while Up < Bottom and Left < Right:
            x = Left
            for x in range(x, Right):
                result.append(matrix[y][x])
            Up += 1

            if Up >= Bottom:
                break
            x = Right - 1
            y = Up
            for y in range(y, Bottom):
                result.append(matrix[y][x])
            Right -= 1

            if Left >= Right:
                break
            y = Bottom - 1
            x = Right - 1
            for x in range(x, Left - 1, -1):
                result.append(matrix[y][x])
            Bottom -= 1

            if Up >= Bottom:
                break
            x = Left
            for y in range(Bottom - 1, Up - 1, -1):
                result.append(matrix[y][x])
            Left += 1
        return result