# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    n=len(first_sequence)
    m=len(second_sequence)
    o=len(third_sequence)
    edit_array=[[[0]*(o+1) for i in range(n+1)] for j in range(m+1)]
    temp=[0]*7
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if i == j == k == 0:
                    continue
                if i > 0:
                    temp[0] = edit_array[i-1][j][k]
                if j > 0:
                    temp[1] = edit_array[i][j-1][k]
                if i > 0 and j > 0:
                    temp[2] = edit_array[i-1][j-1][k]
                if k > 0:
                    temp[3] = edit_array[i][j][k-1]
                if i > 0 and k > 0:
                    temp[4] = edit_array[i-1][j][k-1]
                if k>0 and j>0:
                    temp[5] = edit_array[i][j-1][k-1]
                if i>0 and j>0 and k>0:
                    if second_sequence[i-1] == first_sequence[j-1] == third_sequence[k-1]:
                        temp[6] = edit_array[i-1][j-1][k-1]+1
                    else:
                        temp[6] = edit_array[i-1][j-1][k-1]
                edit_array[i][j][k]=max(temp)
                temp=[0]*7
    return edit_array[m][n][o]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
