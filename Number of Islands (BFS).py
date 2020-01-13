def numIslands(grid: List[List[str]]) -> int: 
        #check if there is any item in the grid 
        if not grid:
                return 0
        #create useful variables
        queue=[]
        count=0
        row = len(grid)
        col = len(grid[0])
        
        #Traverse through the grid, row by row (BFS)
        for i in range (row):
                for j in range (col):
                        #if not land, pass and go to next value
                        if grid[i][j] != '1':
                                continue
                        #increase count, append position in the queue and update '1' to '2'
                        count += 1
                        queue.append((i,j))
                        grid[i][j]='2'
                        
                        #for item in queue, check for connected 1's, add position of connected 1 to queue, and update '1' to '2'
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
