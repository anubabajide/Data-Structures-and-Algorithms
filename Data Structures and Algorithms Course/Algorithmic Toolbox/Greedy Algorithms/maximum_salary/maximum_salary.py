# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    def mySort(numbers):
        if len(numbers) >1:
            mid = len(numbers)//2
            L = numbers[:mid]
            R = numbers[mid:]

            mySort(L)
            mySort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if int(str(L[i]) + str(R[j])) > int(str(R[j]) + str(L[i])):
                    numbers[k] = L[i]
                    i+=1
                else:
                    numbers[k] = R[j]
                    j+=1
                k+=1

            while i < len(L):
                numbers[k] = L[i]
                i+=1
                k+=1

            while j < len(R):
                numbers[k] = R[j]
                j+=1
                k+=1

    mySort(numbers)
    ans = str(numbers[0])
    i = 1
    while i < len(numbers):
        ans += str(numbers[i])
        i += 1

    return int(ans)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
