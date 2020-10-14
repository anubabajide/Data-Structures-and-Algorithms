# Primitive Calculator

## Description 
You are given a primitive calculator that can perform the following three operations with the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.

## Details
**Task**<br>
Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.

**Input format**<br> 
The input consists of a single integer 1 ≤ 𝑛 ≤ 10<sup>6</sup>

**Output format:**<br> 
In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1. In the second line output a sequence of intermediate numbers. That is, the second line should contain positive integers 𝑎<sub>0</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑘−1</sub> such that 𝑎<sub>0</sub> = 1, 𝑎<sub>𝑘−1</sub> = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, 𝑎<sub>𝑖+1</sub> is equal to either 𝑎<sub>𝑖</sub> + 1, 2𝑎<sub>𝑖</sub>, or 3𝑎<sub>𝑖</sub>. If there are many such sequences, output any one of them.


**Constraints:**<br> 
1 ≤ money ≤ 10<sup>3</sup>

## Samples.
Sample 1.

    Input:
        2
    Output:
        2
    
    2 = 1 + 1.

Sample 2.

    Input:
        34
    Output:
        9
    
    34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4.
