# Set with range Sums.

## Description 
In this problem, your goal is to implement a data structure to store a set of integers and quickly compute range sums.

## Details
**Task**<br>
Task. Implement a data structure that stores a set 𝑆 of integers with the following allowed operations:
1. add(𝑖) — add integer 𝑖 into the set 𝑆 (if it was there already, the set doesn’t change). 
2. del(𝑖) — remove integer 𝑖 from the set 𝑆 (if there was no such element, nothing happens).
3. find(𝑖) — check whether 𝑖 is in the set 𝑆 or not.
4. sum(𝑙, 𝑟) — output the sum of all elements 𝑣 in 𝑆 such that 𝑙 ≤ 𝑣 ≤ 𝑟.


**Input format**<br> 
Initially the set 𝑆 is empty. The first line contains 𝑛 — the number of operations. The next
𝑛 lines contain operations. Each operation is one of the following:
1. “+ i" — which means add some integer (not 𝑖, see below) to 𝑆,
2. “- i" — which means del some integer (not 𝑖, see below)from 𝑆,
3. “? i" — which means find some integer (not 𝑖, see below)in 𝑆,
4. “s l r" — which means compute the sum of all elements of 𝑆 within some range of values (not from 𝑙 to 𝑟, see below).

However, to make sure that your solution can work in an online fashion, each request will actually depend on the result of the last sum request. Denote 𝑀 = 1 000 000 001. At any moment, let 𝑥 be the result of the last sum operation, or just 0 if there were no sum operations before. Then
1. “+ i" means add((𝑖 + 𝑥) mod 𝑀),
2. “- i" means del((𝑖 + 𝑥) mod 𝑀),
3. “? i" means find((𝑖 + 𝑥) mod 𝑀),
4. “s l r" means sum((𝑙 + 𝑥) mod 𝑀,(𝑟 + 𝑥) mod 𝑀).

**Output format:**<br> 
For each find request, just output “Found" or “Not found" (without quotes; note that the first letter is capital) depending on whether (𝑖 + 𝑥) mod 𝑀 is in 𝑆 or not. For each sum query, output the sum of all the values 𝑣 in 𝑆 such that ((𝑙+𝑥) mod 𝑀) ≤ 𝑣 ≤ ((𝑟+𝑥) mod 𝑀) (it is guaranteed that in all the tests ((𝑙 + 𝑥) mod 𝑀) ≤ ((𝑟 + 𝑥) mod 𝑀)), where 𝑥 is the result of the last sum operation or 0 if there was no previous sum operation.


**Constraints:**<br>
1 ≤ 𝑛 ≤ 100 000<br>
0 ≤ 𝑖 ≤ 10<sup>9</sup> <br>

## Samples.
Sample 1.

    Input:
        15
        ? 1
        + 1
        ? 1
        + 2
        s 1 2
        + 1000000000
        ? 1000000000
        - 1000000000
        ? 1000000000
        s 999999999 1000000000
        - 2
        ? 2
        - 0
        + 9
        s 0 9
    Output:
        Not found
        Found
        3
        Found
        Not found
        1
        Not found
        10
    
    Explanation:
    For the first 5 queries, 𝑥 = 0. For the next 5 queries, 𝑥 = 3. For the next 5 queries, 𝑥 = 1. The actual list of operations is:
        find(1)
        add(1)
        find(1)
        add(2)
        sum(1, 2) → 3
        add(2)
        find(2) → Found
        del(2)
        find(2) → Not found
        sum(1, 2) → 1
        del(3)
        find(3) → Not found
        del(1)
        add(10)
        sum(1, 10) → 10

    Adding the same element twice doesn’t change the set. Attempts to remove an element which is not in the set are ignored.

Sample 2.

    Input:
        5
        ? 0
        + 0
        ? 0
        - 0
        ? 0
    Output:
        Not found
        Found
        Not found
    
    First, 0 is not in the set. Then it is added to the set. Then it is removed from the set.

Sample 3.

    Input:
        5
        + 491572259
        ? 491572259
        ? 899375874
        s 310971296 877523306
        + 352411209
    Output:
        Found
        Not found
        491572259
    
    Explanation:
    First, 491572259 is added to the set, then it is found there. Number 899375874 is not in the set. The only number in the set is now 491572259, and it is in the range between 310971296 and 877523306, so the sum of all numbers in this range is equal to 491572259.
