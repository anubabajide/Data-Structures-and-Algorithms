# Binary Search

## Description 
In this problem, you will implement the binary search algorithm that allows searching
very efficiently (even huge) lists, provided that the list is sorted.

## Details
**Task**<br> 
The goal in this code problem is to implement the binary search algorithm.

**Input format**<br> 
The first line of the input contains an integer 𝑛 and a sequence 𝑎<sub>0</sub> < 𝑎<sub>1</sub> < . . . < 𝑎<sub>𝑛−1</sub> of 𝑛 pairwise distinct positive integers in increasing order. The next line contains an integer 𝑘 and 𝑘
positive integers 𝑏<sub>0</sub>, 𝑏<sub>1</sub>, . . . , 𝑏<sub>𝑘−1</sub>.


**Output format:**<br> 
For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎<sub>𝑗</sub> = 𝑏<sub>𝑖</sub> or −1 if there is no such index.


**Constraints:**<br> 
1 ≤ 𝑘 ≤ 10<sup>5</sup><br>
1 ≤ 𝑛 ≤ 3 · 10<sup>4</sup><br>
1 ≤ 𝑎<sub>𝑖</sub> ≤ 10<sup>9</sup><br>
for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏<sub>𝑗</sub> ≤ 10<sup>9</sup><br>
for all 0 ≤ 𝑗 < 𝑘;

## Samples.
Sample 1.

    Input:
        5 1 5 8 12 13
        5 8 1 23 1 11
    Output:
        2 0 -1 0 -1
    
    In this sample, we are given an increasing sequence 𝑎0 = 1, 𝑎1 = 5, 𝑎2 = 8, 𝑎3 = 12, 𝑎4 = 13 of length five and five keys to search: 8, 1, 23, 1, 11. We see that 𝑎2 = 8 and 𝑎0 = 1, but the keys 23 and 11 do not appear in the sequence 𝑎. For this reason, we output a sequence 2, 0, −1, 0, −1.
