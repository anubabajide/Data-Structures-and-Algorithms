# python3


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    import math
    import operator

    def Min_And_Max(i,j):
        temp_min=math.inf
        temp_max=-math.inf
        for k in range(i, j):
            #print(M[i][k], M[k+1][j], m[i][k], m[k+1][j])
            a= op[k](M[i][k], M[k+1][j])
            b= op[k](M[i][k], m[k+1][j])
            c= op[k](m[i][k], M[k+1][j])
            d= op[k](m[i][k], m[k+1][j])
            temp_min = min(temp_min, a, b, c, d)
            temp_max = max(temp_max, a, b, c, d)
        return temp_min, temp_max

    a=len(dataset)
    n=math.ceil(a/2)
    m=[[0]*(n+1) for i in range(n+1)]
    M=[[0]*(n+1) for i in range(n+1)]
    d=[0]
    op=[0]

    for i in range(a):
        if i%2==0:
            d.append(int(dataset[i]))
        else:
            if dataset[i]=='+':
                op.append(operator.add)
            elif dataset[i]=='-':
                op.append(operator.sub)
            else:
                op.append(operator.mul)

    for i in range(1, n+1):
        m[i][i] = d[i]
        M[i][i] = d[i]

    for s in range(1, n):
        for i in range(1, n-s+1):
            j = i + s
            m[i][j], M[i][j] = Min_And_Max(i,j)

    return M[1][n]


if __name__ == "__main__":
    print(find_maximum_value(input()))
