# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    import math
    n=len(first_sequence)
    m=len(second_sequence)
    edit_array=[[0]*(n+1) for i in range(m+1)]
    temp=[0]*3
    for i in range(m+1):
        for j in range(n+1):
            if i==j==0:
                continue
            if i>0:
                temp[0]=edit_array[i-1][j]
            if j>0:
                temp[1]=edit_array[i][j-1]
            if i>0 and j>0:
                if second_sequence[i-1]==first_sequence[j-1]:
                    temp[2]=edit_array[i-1][j-1]+1
                else:
                    temp[2]=edit_array[i-1][j-1]
            edit_array[i][j]=max(temp)
            temp=[0]*3
    return edit_array[m][n]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
