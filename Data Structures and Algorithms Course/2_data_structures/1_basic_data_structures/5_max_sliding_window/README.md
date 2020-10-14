# Maximum in Sliding Window

## Description 
Given a sequence 𝑎1, . . . , 𝑎𝑛 of integers and an integer 𝑚 ≤ 𝑛, find the maximum among {𝑎𝑖 , . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1. A naive 𝑂(𝑛𝑚) algorithm for solving this problem scans each window separately. Your goal is to design an 𝑂(𝑛) algorithm.

## Details
**Task**<br>
The first line contains an integer 𝑛, the second line contains 𝑛 integers 𝑎1, . . . , 𝑎𝑛 separated by spaces, the third line contains an integer 𝑚.

**Input format**<br> 
The first line of the input contains the number 𝑞 of queries. Each of the following 𝑞 lines specifies a query of one of the following formats: push v, pop, or max.

**Output format:**<br> 
Output max{𝑎𝑖, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1.

**Constraints:**<br> 
1 ≤ 𝑛 ≤ 10<sup>5</sup> <br>
1 ≤ 𝑚 ≤ 𝑛 <br>
0 ≤ 𝑎<sub>𝑖</sub> ≤ 10<sup>5</sup> <br>
for all 1 ≤ 𝑖 ≤ 𝑛.

## Samples.
Sample 1.

    Input:
        8
        2 7 3 1 5 2 6 2
        4
    Output:
        7 7 5 6 6

