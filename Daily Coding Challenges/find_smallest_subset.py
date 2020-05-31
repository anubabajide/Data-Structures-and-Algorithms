def find_smallest_subset(array):
    array.sort(reverse = True)
    
    set1 = [array[0]]
    set2 = []
    sum1 = array[0]
    sum2 = 0

    for i in range(1, len(array)):
        if sum1 > sum2:
            sum2 += array[i]
            set2.append(array[i])
        else:
            sum1 += array[i]
            set1.append(array[i])

    return set1, set2

if __name__ == '__main__':
    print(find_smallest_subset(list(map(int, input().split()))))
