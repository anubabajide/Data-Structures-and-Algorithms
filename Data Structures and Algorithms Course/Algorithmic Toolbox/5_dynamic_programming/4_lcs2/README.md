# Longest Common Substring of two sequences

## Description 
Compute the length of a longest common subsequence of two sequences.

## Details
**Task**<br>
Given two sequences <br>
𝐴 = (𝑎<sub>1</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑛</sub>) and <br>
𝐵 = (𝑏<sub>1</sub>, 𝑏<sub>2</sub>, . . . , 𝑏<sub>𝑚</sub>), <br>
find the length of their longest common subsequence, i.e., the largest non-negative integer 𝑝 such that there exist indices <br>
1 ≤ 𝑖<sub>1</sub> < 𝑖<sub>2</sub> < · · · < 𝑖<sub>𝑝</sub> ≤ 𝑛 and<br>
1 ≤ 𝑗<sub>1</sub> < 𝑗<sub>2</sub> < · · · < 𝑗<sub>𝑝</sub> ≤ 𝑚, <br>
such that <br>
𝑎<sub>𝑖1</sub> = 𝑏<sub>𝑗1</sub>, . . . , 𝑎<sub>𝑖𝑝</sub> = 𝑏<sub>𝑗𝑝</sub>.

**Input format**<br> 
First line: 𝑛.<br>
Second line: 𝑎<sub>1</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑛</sub>.<br> 
Third line: 𝑚. <br>
Fourth line: 𝑏<sub>1</sub>, 𝑏<sub>2</sub>, . . . , 𝑏<sub>𝑚</sub>

**Output format:**<br> 
Output 𝑝.

**Constraints:**<br> 
1 ≤ 𝑛, 𝑚 ≤ 100;<br>
−10<sup>9</sup> < 𝑎𝑖, 𝑏𝑖 < 10<sup>9</sup>.

## Samples.
Sample 1.

    Input:
        3
        2 7 5
        2
        2 5
    Output:
        2
    
    A common subsequence of length 2 is (2, 5).

Sample 2.

    Input:
        1
        7
        4
        1 2 3 4
    Output:
        0
    
    The two sequences do not share elements.

Sample 3.

    Input:
        4
        2 7 8 3
        4
        5 2 8 7
    Output:
        2
    
    One common subsequence is (2, 7). Another one is (2, 8).
