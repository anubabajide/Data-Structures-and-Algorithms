def gameOfLife(board):
	#Create dictionary to stor info about all neighbours
    a={}
    row=len(board)
    col=len(board[0])

    #helper function to generate info about neighbours
    def getneighbours(i,j):
        b={0:0,1:0}
        if i>0:
            b[board[i-1][j]]+=1
        if i<row-1:
            b[board[i+1][j]]+=1
        if j>0:
            b[board[i][j-1]]+=1
        if j<col-1:
            b[board[i][j+1]]+=1
        if i>0 and j>0:
            b[board[i-1][j-1]]+=1
        if i<row-1 and j<col-1:
            b[board[i+1][j+1]]+=1
        if i>0 and j<col-1:
            b[board[i-1][j+1]]+=1
        if i<row-1 and j>0:
            b[board[i+1][j-1]]+=1
        return b[1]
    
    #generate info for all cells
    for i in range(row):
        for j in range(col):
            a[(i,j)]=getneighbours(i,j)
    
    #update cells based on update
    for i in range(row):
        for j in range(col):
            if board[i][j]==1:
                if not 1<a[(i,j)]<4:
                    board[i][j]=0
            else:
                if a[(i,j)]==3:
                    board[i][j]=1