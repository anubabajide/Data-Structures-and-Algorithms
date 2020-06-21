# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n<2:
        return n

    def pisano_period(m):
        fib_List=[1,1]
        count=1
        while not(fib_List[0]==0 and fib_List[1]==1):
            temp=fib_List[1]
            fib_List[1]=(fib_List[0]+fib_List[1])%m
            fib_List[0]=temp
            count+=1
        return count
    
    fib_num=n%pisano_period(m)
    if fib_num<2:
        return fib_num

    fib_List=[0,1]
    for i in range(fib_num-1):
        temp=fib_List[1]
        fib_List[1]=(fib_List[0]+fib_List[1])%m
        fib_List[0]=temp
    return fib_List[1]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_m))
