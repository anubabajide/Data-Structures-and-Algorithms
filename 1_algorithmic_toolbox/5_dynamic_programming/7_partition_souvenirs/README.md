# Partition Souvenirs

## Description 
You and two of your friends have just returned back home after visiting various countries. Now you would like to evenly split all the souvenirs that all three of you bought.

## Details
**Input format**<br> 
The first line contains an integer 𝑛. The second line contains integers 𝑣1, 𝑣2, . . . , 𝑣𝑛 separated by spaces.

**Output format:**<br> 
Output 1, if it possible to partition 𝑣1, 𝑣2, . . . , 𝑣𝑛 into three subsets with equal sums, and 0 otherwise.

**Constraints:**<br> 
1 ≤ 𝑛 ≤ 20, 1 ≤ 𝑣<sub>𝑖</sub> ≤ 30 for all 𝑖.

## Samples.
Sample 1.

    Input:
        4
        3 3 3 3
    Output:
        0

Sample 2.

    Input:
        1
        40
    Output:
        0

Sample 3.
    
    Input:
    11
    17 59 34 57 17 23 67 1 18 2 59
    Output:
    1
    
    34 + 67 + 17 = 23 + 59 + 1 + 17 + 18 = 59 + 2 + 57.

Sample 4.
    
    Input:
        13
        1 2 3 4 5 5 7 7 8 10 12 19 25
    Output:
       1
    
    1 + 3 + 7 + 25 = 2 + 4 + 5 + 7 + 8 + 10 = 5 + 12 + 19.
