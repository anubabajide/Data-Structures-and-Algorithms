# Improving Quick Sort

## Description 
The goal in this problem is to redesign a given implementation of the randomized quick sort algorithm so that it works fast even on sequences containing many equal elements.

## Details
**Task**<br> 
To force the given implementation of the quick sort algorithm to efficiently process sequences with few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.


**Input format**<br> 
The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 integers 𝑎<sub>0</sub> < 𝑎<sub>1</sub> < . . . < 𝑎<sub>𝑛−1</sub>.

**Output format:**<br> 
Output this sequence sorted in non-decreasing order.

**Constraints:**<br> 
1 ≤ 𝑛 ≤ 10<sup>5</sup><br>
1 ≤ 𝑎<sub>𝑖</sub> ≤ 10<sup>9</sup><br>
for all 0 ≤ 𝑖 < 𝑛

## Samples.
Sample 1.

    Input:
        5
        2 3 9 2 2
    Output:
       2 2 2 3 9
