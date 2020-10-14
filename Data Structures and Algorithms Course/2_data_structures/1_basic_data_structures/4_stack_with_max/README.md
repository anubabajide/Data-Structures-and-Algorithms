# Extending Stack Interface

## Description 
Stack is an abstract data type supporting the operations Push() and Pop(). It is not difficult to implement it in a way that both these operations work in constant time. In this problem, you goal will be to implement a stack that also supports finding the maximum value and to ensure that all operations still work in constant time.

## Details
**Task**<br>
Implement a stack supporting the operations Push(), Pop(), and Max().

**Input format**<br> 
The first line of the input contains the number 𝑞 of queries. Each of the following 𝑞 lines specifies a query of one of the following formats: push v, pop, or max.

**Output format:**<br> 
For each max query, output (on a separate line) the maximum value of the stack.

**Constraints:**<br> 
1 ≤ 𝑞 ≤ 400 000<br> 
0 ≤ 𝑣 ≤ 10<sup>5</sup>

## Samples.
Sample 1.

    Input:
        5
        push 2
        push 1
        max
        pop
        max
    Output:
        2
        2
    Explanation:
    After the first two push queries, the stack contains elements 1 and 2. After the pop query, the element 1 is removed.

Sample 2.

    Input:
        5
        push 1
        push 2
        max
        pop
        max
    Output:
        2
        1
        12

Sample 3.

    Input:
        10
        push 2
        push 3
        push 9
        push 7
        push 2
        max
        max
        max
        pop
        max
    Output:
        9
        9
        9
        9

Sample 4.

    Input:
        3
        push 1
        push 7
        pop
    Output:
    
    Explanation:
    The output is empty since there are no max queries.

Sample 5.

    Input:
        6
        push 7
        push 1
        push 7
        max
        pop
        max
    Output:
        7
        7
