# Number of Inversions

## Description 
An inversion of a sequence 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such that 𝑎𝑖 > 𝑎𝑗 . The number of inversions of a sequence in some sense measures how close the sequence is to being sorted. For example, a sorted (in non-descending order) sequence contains no inversions at all, while in a sequence sorted in descending order any two elements constitute an inversion (for a total of 𝑛(𝑛 − 1)/2 inversions).

## Details
**Task**<br> 
The goal in this problem is to count the number of inversions of a given sequence.

**Input format**<br> 
The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 integers 𝑎<sub>0</sub> < 𝑎<sub>1</sub> < . . . < 𝑎<sub>𝑛−1</sub>.

**Output format:**<br> 
Output the number of inversions in the sequence

**Constraints:**<br> 
1 ≤ 𝑛 ≤ 10<sup>5</sup><br>
1 ≤ 𝑎<sub>𝑖</sub> ≤ 10<sup>9</sup><br>
for all 0 ≤ 𝑖 < 𝑛

## Samples.
Sample 1.

    Input:
        5
        2 3 9 2 9
    Output:
        2
    
    The two inversions here are (1, 3) (𝑎1 = 3 > 2 = 𝑎3) and (2, 3) (𝑎2 = 9 > 2 = 𝑎3)
