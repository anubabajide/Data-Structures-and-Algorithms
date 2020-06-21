# python3


def edit_distance(first_string, second_string):
    import math
    n=len(first_string)
    m=len(second_string)
    edit_array=[[0]*(n+1) for i in range(m+1)]
    temp=[math.inf]*3
    for i in range(m+1):
        for j in range(n+1):
            if i==j==0:
                continue
            if i>0:
                temp[0]=edit_array[i-1][j] +1
            if j>0:
                temp[1]=edit_array[i][j-1] +1
            if i>0 and j>0:
                if second_string[i-1]==first_string[j-1]:
                    temp[2]=edit_array[i-1][j-1]
                else:
                    temp[2]=edit_array[i-1][j-1] + 1
            edit_array[i][j]=min(temp)
            temp=[math.inf]*3
    return edit_array[m][n]



if __name__ == "__main__":
    print(edit_distance(input(), input()))
