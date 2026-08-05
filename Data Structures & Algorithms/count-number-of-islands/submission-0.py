class Solution:


    
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        islands = 0
        for x in range(row):
            for y in range(column):
                def dfs(x,y):
                    if x < 0 or x >= row or y<0 or y >= column:
                        return
                    elif grid[x][y] == "1":
                        grid[x][y] = "0"
                    else:
                        return
                    dfs(x+1,y)
                    dfs(x-1,y)
                    dfs(x,y+1)
                    dfs(x,y-1)
                if grid[x][y] == "1":
                    islands += 1
                    dfs(x,y)
        return islands
