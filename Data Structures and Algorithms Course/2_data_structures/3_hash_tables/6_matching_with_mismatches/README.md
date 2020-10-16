# Pattern Matching with Mismatches

## Description 
A natural generalization of the pattern matching problem is the following: find all text locations where distance from pattern is sufficiently small. This problems has applications in text searching (where mismatches
correspond to typos) and bioinformatics (where mismatches correspond to mutations).

## Details
**Task**<br>
For an integer parameter 𝑘 and two strings 𝑡 = 𝑡<sub>0</sub>𝑡<sub>1</sub> · · ·𝑡<sub>𝑚−1</sub> and 𝑝 = 𝑝<sub>0</sub>𝑝<sub>1</sub> · · · 𝑝<sub>𝑛−1</sub>, we say that 𝑝 occurs in 𝑡 at position 𝑖 with at most 𝑘 mismatches if the strings 𝑝 and 𝑡[𝑖 : 𝑖 + 𝑝) = 𝑡<sub>𝑖</sub>𝑡<sub>𝑖+1</sub> · · ·𝑡<sub>𝑖+𝑛−1</sub> differ in at most 𝑘 positions.

**Input format**<br> 
Every line of the input contains an integer 𝑘 and two strings 𝑡 and 𝑝 consisting of lower case Latin letters.

**Output format:**<br> 
For each triple (𝑘, 𝑡, 𝑝), find all positions 0 ≤ 𝑖<sub>1</sub> < 𝑖<sub>2</sub> < · · · < 𝑖<sub>𝑙</sub> < |𝑡| where 𝑝 occurs in 𝑡 with at most 𝑘 mismatches. Output 𝑙 and 𝑖<sub>1</sub>, 𝑖<sub>2</sub>, . . . , 𝑖<sub>𝑙</sub>.

**Constraints:**<br>
0 ≤ 𝑘 ≤ 5 <br>
1 ≤ |𝑡| ≤ 200 000 <br> 
1 ≤ |𝑝| ≤ min{|𝑡|, 100 000} <br> 
The total length of all 𝑡’s does not exceed 200 000, the total length of all 𝑝’s does not exceed 100 000.


## Samples.
Sample 1.
    
    Input:
        0 ababab baaa
        1 ababab baaa
        1 xabcabc ccc
        2 xabcabc ccc
        3 aaa xxx
    Output:
        0
        1 1
        0
        4 1 2 3 4
        1 0

    Explanation:
    For the first triple, there are no exact matches. For the second triple, baaa has distance one from thepattern. For the third triple, there are no occurrences with at most one mismatch. For the fourth triple,any (length three) substring of 𝑝 containing at least one c has distance at most two from 𝑡. For the fifth triple, 𝑡 and 𝑝 differ in three positions.
