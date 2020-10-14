# Longest Common Substring of Three sequences 

## Description 
Compute the length of a longest common subsequence of two sequences.

## Details
**Task**<br>
Given three sequences <br>
𝐴 = (𝑎<sub>1</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑛</sub>),<br> 
𝐵 = (𝑏<sub>1</sub>, 𝑏<sub>2</sub>, . . . , 𝑏<sub>𝑚</sub>) and <br>
𝐶 = (𝑐<sub>1</sub>, 𝑐<sub>2</sub>, . . . , 𝑐<sub>𝑙</sub>), <br>
find the length of their longest common subsequence, i.e., the largest non-negative integer 𝑝 such that there exist indices <br>
1 ≤ 𝑖<sub>1</sub> < 𝑖<sub>2</sub> < · · · < 𝑖<sub>𝑝</sub> ≤ 𝑛, <br>
1 ≤ 𝑗<sub>1</sub> < 𝑗<sub>2</sub> < · · · < 𝑗<sub>𝑝</sub> ≤ 𝑚, <br>
1 ≤ 𝑘<sub>1</sub> < 𝑘<sub>2</sub> < · · · < 𝑘<sub>𝑝</sub> ≤ 𝑙, <br>
such that <br>
𝑎<sub>𝑖1</sub> = 𝑏<sub>𝑗1</sub> = 𝑐<sub>𝑘1</sub>, . . . , 𝑎<sub>𝑖𝑝</sub> = 𝑏<sub>𝑗𝑝</sub>= 𝑐<sub>𝑘𝑝</sub>


**Input format**<br> 
First line: 𝑛.<br>
Second line: 𝑎<sub>1</sub>, 𝑎<sub>2</sub>, . . . , 𝑎<sub>𝑛</sub>.<br> 
Third line: 𝑚. <br>
Fourth line: 𝑏<sub>1</sub>, 𝑏<sub>2</sub>, . . . , 𝑏<sub>𝑚</sub> <br>
Fifth line: 𝑙. <br>
Sixth line: 𝑐<sub>1</sub>, 𝑐<sub>2</sub>, . . . , 𝑐<sub>𝑙</sub>

**Output format:**<br> 
Output 𝑝.

**Constraints:**<br> 
1 ≤ 𝑛, 𝑚, 𝑙 ≤ 100;<br>
 −10<sup>9</sup> < 𝑎𝑖, 𝑏𝑖 < 10<sup>9</sup>.

## Samples.
Sample 1.

    Input:
        3
        1 2 3
        3
        2 1 3
        3
        1 3 5
    Output:
        2
    
    A common subsequence of length 2 is (1, 3).

Sample 2.

    Input:
        5
        8 3 2 1 7
        7
        8 2 1 3 8 10 7
        6
        6 8 3 1 4 7
    Output:
        3
    
    One common subsequence of length 3 in this case is (8, 3, 7). Another one is (8, 1, 7).
