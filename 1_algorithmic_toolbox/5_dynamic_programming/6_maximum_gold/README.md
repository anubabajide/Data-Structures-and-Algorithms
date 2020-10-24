# Maximum Amount of Gold

## Description 
You are given a set of bars of gold and your goal is to take as much gold as possible into your bag. There is just one copy of each bar and for each bar you can either take it or not (hence you cannot take a fraction of a bar).

## Details
**Task**<br>
Given 𝑛 gold bars, find the maximum weight of gold that fits into a bag of capacity 𝑊.

**Input format**<br> 
The first line of the input contains the capacity 𝑊 of a knapsack and the number 𝑛 of bars of gold. The next line contains 𝑛 integers 𝑤<sub>0</sub>, 𝑤<sub>1</sub>, . . . , 𝑤<sub>𝑛−1</sub> defining the weights of the bars of gold.

**Output format:**<br> 
Output the maximum weight of gold that fits into a knapsack of capacity 𝑊.

**Constraints:**<br> 
1 ≤ 𝑊 ≤ 10<sup>4</sup>; <br>
1 ≤ 𝑛 ≤ 300; <br>
0 ≤ 𝑤<sub>0</sub>, . . . , 𝑤<sub>𝑛−1</sub> ≤ 10<sup>5</sup>.

## Samples.
Sample 1.

    Input:
        10 3
        1 4 8
    Output:
        9
    
    Here, the sum of the weights of the first and the last bar is equal to 9.
