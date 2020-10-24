# Longest Common Substring

## Description 
In the longest common substring problem one is given two strings 𝑠 and 𝑡 and the goal is to find a string 𝑤 of maximal length that is a substring of both 𝑠 and 𝑡. This is a natural measure of similarity between two strings. The problem has applications in text comparison and compression as well as in bioinformatics.<br>The problem can be seen as a special case of the edit distance problem (where only insertions and deletions are allowed). Hence, it can be solved in time 𝑂(|𝑠| · |𝑡|) using dynamic programming. Later in this specialization, we will learn highly non-trivial data structures for solving this problem in linear time 𝑂(|𝑠| + |𝑡|). In this problem, your goal is to use hashing to solve it in almost linear time.


## Details
**Task**<br>
Every line of the input contains two strings 𝑠 and 𝑡 consisting of lower case Latin letters.

**Input format**<br> 
The first line contains a string 𝑠 consisting of small Latin letters. The second line contains the number of queries 𝑞. Each of the next 𝑞 lines specifies a query by three integers 𝑎, 𝑏, and 𝑙.

**Output format:**<br> 
For each pair of strings 𝑠 and 𝑡<sub>𝑖</sub>, find its longest common substring and specify it by outputting three integers: its starting position in 𝑠, its starting position in 𝑡 (both 0-based), and its length. More formally, output integers 0 ≤ 𝑖 < |𝑠|, 0 ≤ 𝑗 < |𝑡|, and 𝑙 ≥ 0 such that 𝑠<sub>𝑖</sub>𝑠<sub>𝑖+1</sub> · · · 𝑠<sub>𝑖+𝑙−1</sub> = 𝑡<sub>𝑗</sub> 𝑡<sub>𝑗+1</sub> · · ·𝑡<sub>𝑗+𝑙−1</sub> and 𝑙 is maximal. (As usual, if there are many such triples with maximal 𝑙, output any of them.)


**Constraints:**<br>
The total length of all 𝑠’s as well as the total length of all 𝑡’s does not exceed 100 000.



## Samples.
Sample 1.

    Input:
        cool toolbox
        aaa bb
        aabaa babbaab
    Output:
        1 1 3
        0 1 0
        0 4 3
    
    Explanation:
    The longest common substring of the first pair of strings is ool, it starts at the first position in toolbox and at the first position in cool. The strings from the second line do not share any non-empty common substrings (in this case, 𝑙 = 0 and one may output any indices 𝑖 and 𝑗). Finally, the last two strings share a substring aab that has length 3 and starts at position 0 in the first string and at position 4 in the second one. Note that for this pair of string one may output 2 3 3 as well.
