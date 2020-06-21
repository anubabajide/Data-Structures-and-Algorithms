# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    n=from_index%60
    m=to_index%60
    fib_List=[0,1]
    sum=0
    for i in range(n-1):
        temp=fib_List[1]
        fib_List[1]=(fib_List[0]+fib_List[1])%10
        fib_List[0]=temp
    a=fib_List[1]
    for i in range(n, 60):
        sum = (sum+fib_List[1])%10
        temp=fib_List[1]
        fib_List[1]=(fib_List[0]+fib_List[1])%10
        fib_List[0]=temp

    fib_List=[0,1]
    for i in range(m):
        sum = (sum+fib_List[1])%10
        temp=fib_List[1]
        fib_List[1]=(fib_List[0]+fib_List[1])%10
        fib_List[0]=temp
    return sum


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
