# Maximum Value of an Arithmetic Value

## Description 
In this problem, your goal is to add parentheses to a given arithmetic
expression to maximize its value.<br>
max(5 − 8 + 7 × 4 − 8 + 9) = ?

## Details
**Task**<br>
Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic operations using additional parentheses.

**Input format**<br> 
The only line of the input contains a string 𝑠 of length 2𝑛 + 1 for some 𝑛, with symbols 𝑠<sub>0</sub>, 𝑠<sub>1</sub>, . . . , 𝑠<sub>2𝑛</sub>. Each symbol at an even position of 𝑠 is a digit (that is, an integer from 0 to 9) while each symbol at an odd position is one of three operations from **{+,-,*}**.

**Output format:**<br> 
Output the maximum possible value of the given arithmetic expression among different
orders of applying arithmetic operations.

**Constraints:**<br> 
0 ≤ 𝑛 ≤ 14 (hence the string contains at most 29 symbols).

## Samples.
Sample 1.

    Input:
        1+5
    Output:
        6

Sample 2.

    Input:
        5-8+7*4-8+9
    Output:
        200
    
    200 = (5 − ((8 + 7) × (4 − (8 + 9))))
