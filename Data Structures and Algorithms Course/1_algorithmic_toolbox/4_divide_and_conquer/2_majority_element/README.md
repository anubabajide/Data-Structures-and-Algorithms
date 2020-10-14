# Majority Element

## Description 
Majority rule is a decision rule that selects the alternative which has a majority, that is, more than half the votes. Given a sequence of elements 𝑎1, 𝑎2, . . . , 𝑎𝑛, you would like to check whether it contains an element that appears more than 𝑛/2 times.

## Details
**Task**<br> 
The goal in this code problem is to check whether an input sequence contains a majority element.

**Input format**<br> 
The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative integers 𝑎<sub>0</sub> < 𝑎<sub>1</sub> < . . . < 𝑎<sub>𝑛−1</sub>.

**Output format:**<br> 
Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times, and 0 otherwise.

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
        1
        2 is the majority element.

Sample 2.

    Input:
        4
        1 2 3 4
    Output:
        0
 
        There is no majority element in this sequence.
 
Sample 3.

    Input:
        4
        1 2 3 1
    Output:
        0
    
    This sequence also does not have a majority element (note that the element 1 appears twice and hence is not a majority element).
