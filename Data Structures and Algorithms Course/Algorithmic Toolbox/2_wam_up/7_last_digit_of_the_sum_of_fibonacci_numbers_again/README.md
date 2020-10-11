# Last Digit of the Sum of Fibonacci Numbers Again

## Description
Now, we would like to find the last digit of a partial sum of Fibonacci numbers: 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.

## Details
**Task** <br>
Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 +
· · · + 𝐹𝑛.

**Input format** <br>
The input consists of two non-negative integers 𝑚 and 𝑛 separated by a space.

**Output format** <br>
Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.

**Constraints** <br>
0 ≤ 𝑚 ≤ 𝑛 ≤ 10<sup>14</sup>


## Samples.
Sample 1.

    Input:
        3 7
    Output:
        1
    
    𝐹3 + 𝐹4 + 𝐹5 + 𝐹6 + 𝐹7 = 2 + 3 + 5 + 8 + 13 = 31.

Sample 2.

    Input:
        10 10
    Output:
        5
    
    𝐹10 = 55.

Sample 3.

    Input:
        10 200
    Output:
        2
    
    𝐹10 + 𝐹11 + · · · + 𝐹200 = 734 544 867 157 818 093 234 908 902 110 449 296 423 262
