"""
so at 1 position check up,left,right,down if it is valid
so let us iterate through the grid then when we encounter our 1st 1 we would do the function

function
if your row is less than 0 or greater than or columns is less than 0 or greater than
    return
elif:
    position is "0"
    return

at your current position
check up down left right
then when done turn your position to "0"

you were correct but always trace your example

"""


class Solution:



    
    def numIslands(self, grid: List[List[str]]) -> int:


        row = len(grid)
        col = len(grid[0])
        counter = 0
        def dfs(x,y):
            if x < 0 or x >= row or y < 0 or y >= col:
                return
            elif grid[x][y] == "0":
                return
            grid[x][y] = "0"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        for x in range(row):
            for y in range(col):
                if grid[x][y] == "0":
                    continue
                dfs(x,y)
                counter+=1
        return counter    