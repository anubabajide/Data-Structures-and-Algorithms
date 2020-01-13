class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 

        if not grid:
            return 0
        
        queue=[]
        count=0
        row = len(grid)
        col = len(grid[0])
        
        for i in range (row):
            for j in range (col):
                if grid[i][j] != '1':
                    continue
                count += 1
                queue.append((i,j))
                grid[i][j]='2'
                
                while queue:
                    x,y=queue.pop(0)
                    if x>0 and grid[x-1][y] == '1':
                        queue.append((x-1,y))
                        grid[x-1][y]='2'
                        
                    if x+1<row and grid[x+1][y] == '1':
                        queue.append((x+1,y))
                        grid[x+1][y]='2'
                        
                    if y>0 and grid[x][y-1] == '1':
                        queue.append((x,y-1))
                        grid[x][y-1]='2'
                        
                    if y+1<col and grid[x][y+1] == '1':
                        queue.append((x,y+1))
                        grid[x][y+1]='2'
        return count
  