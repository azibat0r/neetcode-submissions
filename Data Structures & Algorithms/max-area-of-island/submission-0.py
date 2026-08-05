class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        ma = 0
        for x in range(row):
            for y in range(column):
                def dfs(x,y):
                    if x < 0 or x >= row or y<0 or y >= column:
                        return 0
                    elif grid[x][y] == 1:
                        grid[x][y] = 0
                    else:
                        return 0
                    return (1 + 
                    dfs(x+1,y) +
                    dfs(x-1,y) +
                    dfs(x,y+1) +
                    dfs(x,y-1))
                if grid[x][y] == 1:
                    ca = dfs(x,y)
                    ma = max(ca,ma)
        return ma
